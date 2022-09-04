
from flask_app import app
from flask import Flask, render_template, redirect, request, session,flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_the_dojos = all_dojos)

@app.route('/create/dojo', methods=["POST"])
def dojo_create():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        "name": request.form['name']
    }
    Dojo.create(data)
    return redirect('/')