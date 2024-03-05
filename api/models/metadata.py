from config.db import mysql_connector
import uuid
import json

class MetaData:
    @staticmethod
    def create(tool_id, score, metadata):
        try:
            generated_uuid = str(uuid.uuid4())
            metadata  = json.dumps(metadata)
            print('metadata',metadata)
            query = f""" INSERT INTO tool_metadata(tool_id, score, metadata, uuid)VALUES({tool_id}, {score}, '{metadata}', '{generated_uuid}');"""
            results = mysql_connector.execute_query(query)
            if results:
                return True
            else:
                return False
        except Exception as e:
            print('Exception in metadata create', e)
            return False
        

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

