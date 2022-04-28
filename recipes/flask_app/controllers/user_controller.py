from flask_app import app
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.users import Users
from flask_app.models.recipe import Recipe
# @app.route('/')
# def index():
#     return f"testing"

@app.route('/')
def user():
    return render_template("register.html")
## route to display users

@app.route('/register', methods=['POST'])
def register():
    if not Users.validate_register(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    
    new_user_id = Users.register_user(query_data)
    
    session["user_id"] = new_user_id
    
    return redirect('/')




@app.route('/login', methods=['POST'])
def login():
    if not Users.validate_login(request.form):
    
        return redirect('/')
    
    logged_user = Users.get_by_email(request.form)
    
    session['user_id'] = logged_user.id
        
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("please login or register")
        return redirect('/')
    
    query_data = {
        "user_id" : session["user_id"]
    }
    
    user = Users.get_by_id(query_data)
    all_recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', user = user, all_recipes = all_recipes )
        
        
        
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
