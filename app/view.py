from app import app, db
from flask import render_template, request, redirect, url_for
from app.model import Questao, Opcao, Resposta
import statistics  # <--- Importante: Adicionei essa lib nativa do Python

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/questionario', methods=['POST', 'GET'])
def questionario():
    questoes = Questao.query.order_by('id')
    opcoes = Opcao.query.order_by('id')

    if request.method == 'POST':
        for questao in questoes:
            # Pega o valor do radio button (que é o ID da opção)
            opcao_id = request.form.get(f'questao_{questao.id}')
            if opcao_id:
                resposta = Resposta(questao_fk=questao.id, opcao_fk=int(opcao_id))
                db.session.add(resposta)
        db.session.commit()
        return redirect(url_for('homepage'))

    return render_template('questionario.html', questoes=questoes, opcoes=opcoes)

@app.route('/resultados')
def resultados():
    questoes = Questao.query.order_by('id').all()
    dados = []
    
    for questao in questoes:
        opcoes_texto = []
        votos = []
        
        for opcao in questao.opcoes:
            opcoes_texto.append(opcao.text)
            # Conta quantos votos cada opção teve no banco
            qtd = Resposta.query.filter_by(opcao_fk=opcao.id).count()
            votos.append(qtd)
            
        # --- Cálculos Estatísticos ---
        # Verificamos se tem votos para não dar erro de divisão por zero
        if votos and sum(votos) > 0:
            # 1. Moda: Qual opção teve mais votos?
            max_votos = max(votos)
            # Cria uma lista com os nomes das opções vencedoras (caso haja empate)
            moda_lista = [opcoes_texto[i] for i, v in enumerate(votos) if v == max_votos]
            moda = ", ".join(moda_lista)
            
            # 2. Média: Média aritmética da quantidade de votos por opção
            media = statistics.mean(votos)
            
            # 3. Mediana: O valor central da distribuição dos votos
            mediana = statistics.median(votos)
        else:
            moda = "Ainda sem votos"
            media = 0
            mediana = 0

        dados.append({
            'questao': questao.text,
            'opcoes': opcoes_texto,
            'votos': votos,
            # Passando os dados matemáticos para o HTML
            'moda': moda,
            'media': f"{media:.2f}", # Formatando para 2 casas decimais
            'mediana': mediana
        })
        
    return render_template('resultados.html', dados=dados)

@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')