from unicodedata import category
from market import app
from market import db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():

    #SEM BD
    """items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items )""" #Podemos passar objetos. um mapa por exemplo
    #return render_template('market.html', item_name='Phone')  ->> podemos usar keys para passa-los como parametro e ter acesso ao seu conteúdo dentro do .html com {{ item_name }}

    items = Item.query.all()    
    return render_template('market.html', items=items )

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:  #valida se erro retornou o diccionario vazio ou algum erro
        for err_msg in form.errors.values():
            flash(f'Erro ao criar o user: {err_msg}', category='danger')
    return render_template('register.html', form=form)