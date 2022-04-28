from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojos:
    db = 'dojos_and_ninjas_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.ninjas = []
        
    
    
    
    
    @classmethod
    def create_dojos(cls,data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW());"
        
        result = connectToMySQL(cls.db).query_db(query,data)
        
        return result
    
    
    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        
        results = connectToMySQL(cls.db).query_db(query)
        
        all_dojos = []
        
        for dict in results:
            all_dojos.append(cls(dict))
        return all_dojos
    
    

    
    @classmethod
    def get_dojos_by_id(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojos_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for data in results:
            ninja_data = {
            "id" : data['id'],
            "first_name" : data['first_name'],
            "last_name" : data['last_name'],
            "age" : data['age'],
            "created_at" : data['created_at'],
            "updated_at" : data['updated_at']
            }
            dojo.ninjas.append(ninjas.Ninjas(ninja_data))
        return dojo
        
        
        
        
        
        
        # dojos = []
        
        # for item in result:
        #     dojos.append(Dojos(item))
        