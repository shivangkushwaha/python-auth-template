from config.db import mysql_connector

class Tool:
    
    @staticmethod
    def create(name = None, description = None, instruction = None, capabilities = None, github_link = None, run_commands = None,
               conversation_starters = None, file_path = None, file_size = None, content_type = None, file_extension = None,
               uuid = None):
        query = f""" INSERT INTO tools
                    (name, description, instruction, capabilities, github_link, run_commands, conversation_starters, 
                    file_path, file_size, content_type, file_extension, uuid)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        # Create a tuple of parameters to pass to the execute function
        params = (name, description, instruction, capabilities, github_link, run_commands, conversation_starters,file_path, file_size, content_type, file_extension, uuid)
        
        # Replace None values with NULL
        
        params = [param if param is not None else 'NULL' for param in params]
        
        # execute query
        results = mysql_connector.execute_query(query, params)
        print('results', results)
        return results  

    @staticmethod
    def list(limit, offset):
        try:
            # select then number of records as per params
            select_query = f"SELECT * FROM tools limit {limit} offset {offset}"
            records = mysql_connector.execute_query(select_query)
            
            # getting total number of records
            select_query = f"SELECT COUNT(id) as count from tools;"
            total_records = mysql_connector.execute_query(select_query)
            return records,total_records[0]
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while getting list : {e}")
            return None
    
    @staticmethod
    def details(id):
        try:
            # select then number of records as per params
            select_query = f"SELECT * FROM tools where id = {id}"
            records = mysql_connector.execute_query(select_query)
            return records[0]
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while getting user by ID: {e}")
            return None

