from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.users import Users
from flask_app.models.recipe import Recipe

@app.route('/create/recipe')
def create_recipe():
    if "user_id" not in session:
        flash("please login or register")
        return redirect('/')
    
    return render_template('new_recipe.html')


@app.route('/recipe/new', methods=['POST'])
def new_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/create/recipe')
    
    query_data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date_made" : request.form['date_made'],
        "under_thirty_min" : request.form['under_thirty_min'],
        "user_id" : session['user_id']
    }
    
    Recipe.create_recipe(query_data)
    
    return redirect('/dashboard')


@app.route('/view/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if "user_id" not in session:
        flash("please login or register")
        return redirect('/')
    
    query_data = {
        "recipe_id" : recipe_id
    }
    
    recipe = Recipe.get_one_recipe(query_data)
    
    return render_template("view_recipe.html" , recipe = recipe)
    
    
    
@app.route('/edit/recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if "user_id" not in session:
        flash("please login or register")
        return redirect('/')
    
    query_data = {
        "recipe_id" : recipe_id
    }
    
    recipe = Recipe.get_one_recipe(query_data)
    return render_template('edit_recipe.html' , recipe = recipe)


@app.route('/update/recipe/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/edit/recipe/{recipe_id}')

    query_data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date_made" : request.form['date_made'],
        "under_thirty_min" : request.form['under_thirty_min'],
        "recipe_id" : recipe_id
    }
    
    Recipe.update_recipe(query_data)
    return redirect('/dashboard')


@app.route('/delete/recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    query_data = {
        "recipe_id" : recipe_id
    }
    
    Recipe.delete_recipe(query_data)
    
    return redirect('/dashboard')
    
# @app.route('/recipe/new' , methods = ['POST'])
# def new_recipe():
#     if not Recipe.validate_recipe(request.form):
#         return redirect('/create/recipe')
    
#     data = {
        # "name" : request.form['name'],
        # "description" : request.form['description'],
        # "instructions" : request.form['instructions'],
        # "user_id" : session['user_id']
#     }
    
#     Recipe.create_recipe(data)
    
    
#     return redirect('/create/recipe')
















# @app.route('/recipe/create', methods=['POST'])
# def create_ninja():
#     query_data = {
#         "first_name" : request.form["first_name"],
#         "last_name" : request.form["last_name"],
#         "age" : request.form["age"],
#         "dojo_id" : request.form["dojo_id"]
#     }
    
#     new_ninja_id = Ninjas.create_ninja(query_data)
    
#     # session['user_id'] = new_ninja_id
     
#     return redirect('/dojos')