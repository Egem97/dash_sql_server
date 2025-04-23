from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Clase de usuario para Flask-Login
class User(UserMixin):
    def __init__(self, username):
        self.id = username
        
# Diccionario de usuarios (en producción esto debería ser una base de datos)
users = {
    'admin': generate_password_hash('admin123')  # Cambia esta contraseña en producción
}

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    if username not in users:
        return None
    return User(username)

def verify_password(username, password):
    if username not in users:
        return False
    return check_password_hash(users[username], password) 