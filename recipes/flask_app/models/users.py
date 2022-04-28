from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Users():
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.hungry = [] #i user many recipes
    
    @staticmethod
    def validate_register(form_data):
        is_valid = True
        if len(form_data["first_name"]) < 1:
            flash("first name must be present")
            is_valid = False
        if len(form_data["last_name"]) < 1:
            flash("last name must be present")
            is_valid = False
        if len(form_data["email"]) < 1:
            flash("email must be present")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data["email"]):
            flash("please enter a valid email")
            is_valid = False
        if len(form_data["password"]) < 8:
            flash("password must be 8 characters long")
            is_valid = False
        if (form_data["password"] != form_data["conf_pass"]):
            flash("password and password confirmation fields must match")
            is_valid = False
            
        return is_valid


    @staticmethod
    def validate_login(form_data):
        is_valid = True
        user_in_db = Users.get_by_email(form_data)
    # user is not registered in the db
        if not user_in_db:
            flash("Invalid Email/Password")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, form_data['password']):
        # if we get False after checking the password
            flash("Invalid Email/Password")
            is_valid = False
        
        return is_valid
        
    @classmethod
    def register_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW());"
        
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])