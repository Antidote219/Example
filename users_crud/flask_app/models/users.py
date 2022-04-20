from flask_app.config.mysqlconnection import connectToMySQL

class Users():
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        
        result = connectToMySQL("users_schema").query_db(query)
        
        user = []
        
        for item in result :
            user.append(Users(item))
            
        return user
        
    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        
        result = connectToMySQL("users_schema").query_db(query, data)
        
        return result
    
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s"
        
        result = connectToMySQL("users_schema").query_db(query, data)
        
        user = Users(result[0])
        
        return user
        # query = "SELECT * FROM users.user.id"
        # result = connectToMySQL("users_schema").query_db(query, data)
        # return result

    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(user_id)s"
        
        result = connectToMySQL("users_schema").query_db(query, data)
        
        
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(user_id)s;'
        
        result = connectToMySQL("users_schema").query_db( query, data )
        
        return connectToMySQL("users_schema").query_db( query, data )




    # def user_update(cls,data):
    #     query = "UPDATE users SET (%(first_name)s, %(last_name)s, %(email)s) WHERE id = %(user.id)s;"
        
    #     result = connectToMySQL("users_schema").query_db(query, data)
    #     return result