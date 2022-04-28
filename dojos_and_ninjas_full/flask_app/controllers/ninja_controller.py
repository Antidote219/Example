from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninjas import Ninjas
from flask_app.models.dojos import Dojos

@app.route("/ninjas")
def ninjas():
     
     
    all_dojos = Dojos.get_all_dojos()
    print(all_dojos)
    
    
    return render_template('ninja.html' , all_dojos = all_dojos)

@app.route('/ninja/new', methods=['POST'])
def create_ninja():
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    
    new_ninja_id = Ninjas.create_ninja(query_data)
    
    # session['user_id'] = new_ninja_id
     
    return redirect('/dojos')