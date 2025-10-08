from app import app, db
from flask import render_template, request, redirect, url_for
from app.model import Questao, Opcao, Resposta
from app.form import RespostaForm

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/questionario', methods=['POST', 'GET'])
def questionario():
    questoes = Questao.query.order_by('id')
    opcoes = Opcao.query.order_by('id')
    form = RespostaForm()

    if request.method == 'POST':
        for questao in questoes:
            opcao_id = request.form.get(f'questao_{questao.id}')
            if opcao_id:
                resposta = Resposta(questao_fk=questao.id, opcao_fk=int(opcao_id))
                db.session.add(resposta)
        db.session.commit()
        return redirect(url_for('homepage'))  # Redireciona após o envio

    return render_template('questionario.html', questoes=questoes, opcoes=opcoes, form=form)


@app.route('/resultados')
def resultados():
    questoes = Questao.query.order_by('id').all()
    dados = []
    for questao in questoes:
        opcoes = []
        votos = []
        for opcao in questao.opcoes:
            opcoes.append(opcao.text)
            votos.append(Resposta.query.filter_by(opcao_fk=opcao.id).count())
        dados.append({
            'questao': questao.text,
            'opcoes': opcoes,
            'votos': votos
        })
    return render_template('resultados.html', dados=dados)

