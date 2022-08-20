from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #chama a instancia do Flask e depois faz referencia ao arquivo do python local que vc esta trabalhando,
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db ' #indica onde a data base esta localizada e configurada. Por convenção 'SQLALCHEMY_DATABASE_URI' é a key e market.db é o nome que queremos pra BD.
app.config['SECRET_KEY'] = '1fdce44bc5d958c04ccb70c8'

db = SQLAlchemy(app)

from market import routes