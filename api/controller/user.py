from api.models.user import User

def get_users():
    return User.get_all_users()

# def get_user_by_id(user_id):
#     return User.get_user_by_id(user_id)

def create_user(name, email):
    return User.create_user(name, email)

# def update_user(user_id, name, email):
#     return User.update_user(user_id, name, email)

# def delete_user(user_id):
#     return User.delete_user(user_id)