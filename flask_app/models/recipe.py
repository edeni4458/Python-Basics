from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
NAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Recipe:

        def __init__(self, data):
                self.id = data['id']
                self.name = data['name']
                self.description = data['description']
                self.instructions = data['instructions']
                self.date_made = data['date_made']
                self.user_id = data['user_id']
                self.first_name = data['first_name']
                self.created_at = data['created_at']
                self.updated_at = data['updated_at']

        @classmethod
        def save(cls, data):
                query = "INSERT INTO recipes (name, description, instructions, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s);"
                return connectToMySQL('recipes').query_db(query, data)
        
        @classmethod
        def get_all(cls):
            query = "SELECT * FROM recipes LEFT JOIN users on users.id = recipes.user_id;"

            results = connectToMySQL('recipes').query_db(query)
            recipes = []

            for r in results:
                recipes.append( cls(r) )
            return recipes
        
        @classmethod
        def get_one_with_users(cls, data ):
            query = "SELECT * FROM recipes LEFT JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;"
            results = connectToMySQL('recipes').query_db(query,data)
            print(results)
            recipe = cls(results[0])
            return recipe

        @classmethod
        def update(cls,data):
            query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE id = %(id)s;"
            return  connectToMySQL('recipes').query_db(query,data)

        @classmethod
        def delete(cls,data):
            query = "DELETE FROM recipes WHERE id = %(id)s;"
            return  connectToMySQL('recipes').query_db(query,data)
            

        @staticmethod
        def validate_recipe(recipe):
            is_valid = True
            if len(recipe['name']) < 3:
                flash("name must be 3 characters")
                is_valid=False
            if len(recipe['description']) < 3:
                flash("description must be 3 characters")
                is_valid=False
            if len(recipe['instructions']) < 3:
                flash("instructions must be 3 characters")
                is_valid=False
            if not 'under_30' in recipe:
                flash("invalid")
                is_valid=False
            if not 'date_made' in recipe:
                flash("invalid")
                is_valid=False
            return is_valid