import mysql.connector
import os
from datetime import datetime
import json
class MySQLConnector:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_DATABASE")


    def connect(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database
        )
        self.cursor = self.cnx.cursor(dictionary = True)


    def disconnect(self):
        self.cursor.close()
        self.cnx.close()


    def execute_query(self, query, params = None):
        try:
            """Execute an insert or select query."""
            self.connect()
            is_select_query = query.strip().lower().startswith("select")
            if params:
                self.cursor.execute(query, params)
                self.cnx.commit()
                result = self.cursor.rowcount if not is_select_query else None
            else:
                print('result in execution',query,params)
                self.cursor.execute(query, params)
                print('result in execution',self.cursor.rowcount)
                if is_select_query:
                    result = self.cursor.fetchall()
                    result = self.formate_results(result)
                else:
                    result = self.cursor.rowcount
            self.disconnect()
            return result
        except Exception as e:
            print('Error in query execution ',e)
            return False


    def formate_results(self, result):
        for row in result:
                    for key, value in row.items():
                        if isinstance(value, datetime):
                            row[key] = value.isoformat()
                        if isinstance(value, str):
                            try:
                                # Try to load the value as JSON
                                row[key] = json.loads(value)
                            except json.JSONDecodeError:
                                pass
        return result



mysql_connector = MySQLConnector()

