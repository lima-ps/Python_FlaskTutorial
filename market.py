from flask import Flask, render_template
app = Flask(__name__) #chama a instancia do Flask e depois faz referencia ao arquivo do python local que vc esta trabalhando, 

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items ) #Podemos passar objetos. um mapa por exemplo
    #return render_template('market.html', item_name='Phone')  ->> podemos usar keys para passa-los como parametro e ter acesso ao seu conteúdo dentro do .html com {{ item_name }}
    