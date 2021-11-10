from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CheckForm(FlaskForm):
    crypto_name = StringField('Crypto')
    check = SubmitField('Check')
