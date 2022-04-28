from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import users
class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty_min = data['under_thirty_min']
        self.user_id = data['user_id']
        
        self.cook = [] # 1 recipe has 1 user
    
    
    @classmethod
    def create_recipe(cls , data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_thirty_min, user_id, created_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_thirty_min)s,%(user_id)s, NOW()) ;"
        
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
        
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
    
        all_recipes_with_user = []
        for item in results:
            recipe = cls(item)
        
            user_data = {
                "id" : item['users.id'],
                "first_name" : item['first_name'],
                "last_name" : item['last_name'],
                "email" : item['email'],
                "password" : item['password'],
                "created_at" : item['users.created_at'],
                "updated_at" : item['users.updated_at'],
            }
            recipe.cook = users.Users(user_data)
            all_recipes_with_user.append(recipe)
        return all_recipes_with_user

    @classmethod
    def get_one_recipe(cls , data):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(recipe_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        
        recipe = cls(results[0])
        
        user_data = {
        "id" : results[0]['users.id'],
        "first_name" : results[0]['first_name'],
        "last_name" : results[0]['last_name'],
        "email" : results[0]['email'],
        "password" : results[0]['password'],
        "created_at" : results[0]['users.created_at'],
        "updated_at" : results[0]['users.updated_at'],
        }
        recipe.cook = users.Users(user_data)
        return recipe
    
    
    
    @classmethod
    def update_recipe(cls,data):
        
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_thirty_min = %(under_thirty_min)s, updated_at = NOW() WHERE id = %(recipe_id)s"
    
        connectToMySQL(cls.db).query_db(query, data)
        
        return
    
    
    
    @classmethod
    def delete_recipe(cls,data):
        
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s"
    
    
        connectToMySQL(cls.db).query_db(query, data)
        
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if len(form_data["name"]) < 3:
            flash("recipe name must be at least 3 characters long")
            is_valid = False
        if len(form_data["description"]) < 3:
            flash("description must be at least 3 characters long")
            is_valid = False
        if len(form_data["instructions"]) < 3:
            flash("instructions must be at least 3 characters long")
            is_valid = False
        # elif not EMAIL_REGEX.match(form_data["email"]):
        #     flash("please enter a valid email")
        #     is_valid = False
        # if len(form_data["password"]) < 8:
        #     flash("password must be 8 characters long")
        #     is_valid = False
        # if (form_data["password"] != form_data["conf_pass"]):
        #     flash("password and password confirmation fields must match")
        #     is_valid = False
            
        return is_valid