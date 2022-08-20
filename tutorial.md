# INSTALL
   * pip install flask

# SET ENVIROMENT
   * set FLASK_APP=market.py    //"market.py" é o ficheiro base criado no projeto
        export FLASK_APP=market.py  //esse se for pela linha de comando do python. nao precisa do comando abaixo
   * $env:FLASK_APP = "market.py"  
   * $env:FLASK_ENV = "development"   //ativa o modo debud, para as modificações acontecrem enquanto trabalhamos e mostrar os erros
        ou: export FLASK_ENV=development  //python bash

# RUN SERVER
   * flask run

# DATABASE

   * pip install flask-sqlalchemy (sqllite)
        - app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db ' #indica onde a data base esta localizada e configurada. Por convenção 'SQLALCHEMY_DATABASE_URI' é a key e market.db é o nome que queremos pra BD.
   * from market import db  //market é o nome do app
   * python (entra na comand line do python)
     - db.create_all()   //gera a BD
     - from market import Item   //inicializa nosso primeiro modelo
     - item1 = Item('name': 'Phone', 'barcode': '893212299897', 'price': 500)  //add primeiro item
     - db.session.add(item1)  //add a tabela
     - db.session.commit()  //salva
     - Item.query.all()  //valida o que foi criado
     - for item in Item.query.filter(price=500)  //filtra basedo em parametros colocados
            item.name
     

