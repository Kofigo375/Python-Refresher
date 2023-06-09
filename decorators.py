user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "qwerty"

#print(get_admin_password())

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())