from app import db

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idade = db.Column(db.Integer)
    genero = db.Column(db.String)


class Questoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String)

class Opcoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    