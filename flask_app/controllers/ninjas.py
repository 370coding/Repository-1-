from flask_app import app
from flask import Flask,render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def createAninja():
    all_dojos = Dojo.get_all()
    return render_template("ninja.html",all_the_dojos = all_dojos)

@app.route('/create_ninja', methods=["POST"])
def createNinja():
    print(request.form)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.create(data)
    return redirect('/')