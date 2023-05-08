
users = {
    'user1': {'username': 'asdc@asd.com' 'password': 'password1'}
    'user2': {'username': 'asde@ddd.com' 'password': 'password12'}
}

def authenticate(func):
    def wrapper(*args, **kwargs):
        username = input("Username: ")
        password = input("Password: ")
        if username in users:
            return func(*args, **kwargs)
        else:
            print("Invalid username or password")
    return wrapper
