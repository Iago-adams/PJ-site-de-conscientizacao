from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from app.model import Questao, Opcao, Resposta
from app import db


class RespostaForm(FlaskForm):
    questao=IntegerField('Questão', validators=[DataRequired()])
    opcao=IntegerField('Opção', validators=[DataRequired()])

    def save(self):
        resposta=Resposta(
            questao_fk = self.questao.data,
            opcao_fk = self.opcao.data
        )
        db.session.add(resposta)
        db.session.commit()
