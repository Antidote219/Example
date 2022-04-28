from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.dojos import Dojos

@app.route("/")
def index():
    return f"testing"

@app.route('/dojos')
def alldojo():
    
    
    all_dojos = Dojos.get_all_dojos()
    print(all_dojos)
    
    
    return render_template ("dojo.html" , all_dojos = all_dojos)

@app.route("/new_dojo" , methods=["POST"])
def new_dojo():
    data = {
        "name" : request.form["dojoname"],
    }
    Dojos.create_dojos(data)
    
    
    return redirect("/dojos")


@app.route('/dojos/<int:dojo_id>')
def showdojos(dojo_id):
    data = {
        'dojos_id' : dojo_id
    }
    dojos = Dojos.get_dojos_by_id(data)
    return render_template('dojo_ninja.html' , dojo = dojos )