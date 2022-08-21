from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__) #chama a instancia do Flask e depois faz referencia ao arquivo do python local que vc esta trabalhando,
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db ' #indica onde a data base esta localizada e configurada. Por convenção 'SQLALCHEMY_DATABASE_URI' é a key e market.db é o nome que queremos pra BD.
app.config['SECRET_KEY'] = '1fdce44bc5d958c04ccb70c8'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"  #direciona o cliente para a página de login se ele tentar aceder a uma página restrita a user logados
login_manager.login_message_category = 'info'


from market import routes