from app import db

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    opcoes = db.relationship('Opcao', backref='questao', lazy=True)


class Opcao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    questao_fk = db.Column(db.Integer, db.ForeignKey('questao.id', name='fk_opcao_questao'))


class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questao_fk = db.Column(db.Integer, db.ForeignKey('questao.id', name='fk_resposta_questao'))
    opcao_fk = db.Column(db.Integer, db.ForeignKey('opcao.id', name='fk_resposta_opcao'))

