from config.db import mysql_connector
# mysql_connector = MySQLConnector()

class User:
    @staticmethod
    def get_all_users():
        try:
            select_query = "SELECT * FROM customers"
            return mysql_connector.execute_query(select_query)
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while getting all users: {e}")
            return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            select_query = "SELECT * FROM user WHERE id = %s"
            return mysql_connector.execute_query(select_query, (user_id,))
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while getting user by ID: {e}")
            return None

    @staticmethod
    def create_user(name, email):
        try:
            insert_query = "INSERT INTO user (name, email) VALUES (%s, %s)"
            return mysql_connector.execute_query(insert_query, (name, email))
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while creating user: {e}")
            return None

    @staticmethod
    def update_user(user_id, name, email):
        try:
            update_query = "UPDATE user SET name = %s, email = %s WHERE id = %s"
            return mysql_connector.execute_query(update_query, (name, email, user_id))
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while updating user: {e}")
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            delete_query = "DELETE FROM user WHERE id = %s"
            return mysql_connector.execute_query(delete_query, (user_id,))
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while deleting user: {e}")
            return None
