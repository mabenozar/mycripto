from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired


class FormPurchase(FlaskForm):
    coins           = ['EUR','ETH','LTC','BNB','EOS','XLM','TRX','BTC','XRP','BCH','USDT','BSV','ADA']
    selectFrom      = SelectField('From', validators=[DataRequired()], choices=coins)
    selectTo        = SelectField('To', validators=[DataRequired()], choices=coins)
    quantityFrom    = FloatField('Quantity From:', validators=[DataRequired()])
    purchase        = SubmitField('Purchase')





