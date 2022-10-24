# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from asyncio import Task
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Games, Customers
from application.forms import GameForm, CustomerForm

#READ BOTH DATABASES
@app.route('/', methods=['POST', 'GET'])
def index():
    games = Games.query.all()
    customers = Customers.query.all()
    return render_template('index.html', title="Current Reservations", games=games, customers=customers)

# CREATE game items 
@app.route('/addgame', methods=['POST', 'GET'])
def listadd():
    form = GameForm() 
    if form.validate_on_submit(): 
        games = Games(
            name = form.name.data
        )
        db.session.add(games)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addgame.html', title="Add a new game", form=form)

#CREATE customer items
@app.route('/reservegame', methods=['POST','GET'])
def add():
    form = CustomerForm()
    if form.validate_on_submit():
        customers = Customers(
            name = form.name.data,
            table = form.table.data,
            fk_gid = form.fk_gid.data
        )
        db.session.add(customers)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('reservegame.html', title="Please reserve a game", form=form)

#UPDATE game items
@app.route('/updategame/<int:gid>', methods=['GET', 'POST'])
def updategame(gid):
    form = GameForm()

    games = Games.query.get(gid)

    if form.validate_on_submit():
        games.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = games.name
    return render_template('updategame.html', title='Update a game', form=form)

#UPDATE customer items
@app.route('/updatereservation/<int:cid>', methods=['GET', 'POST'])
def update(cid):
    form = CustomerForm()
    customers = Customers.query.get(cid)
    if form.validate_on_submit():
        customers.name = form.name.data
        customers.table = form.table.data
        customers.fk_gid = form.fk_gid.data
        db.session.commit() 
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = customers.name 
        form.fk_gid.data = customers.fk_gid
    return render_template('updatereservation.html', title='Update your reservation', form=form)


#DELETE game items
@app.route('/removegame/<int:gid>')
def removegame(gid):
    games = Games.query.get(gid)
    db.session.delete(games)
    db.session.commit()
    return redirect(url_for('index'))

#DELETE customer items
@app.route('/cancelorder/<int:cid>')
def delete(cid):
    customers = Customers.query.get(cid)
    db.session.delete(customers)
    db.session.commit()
    return redirect(url_for('index'))