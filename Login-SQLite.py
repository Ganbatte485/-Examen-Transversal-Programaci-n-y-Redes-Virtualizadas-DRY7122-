from flask import Flask, request, redirect
import sqlite3
import hashlib
import os

app = Flask(__name__)
DB_FILE = "usuarios.db"

def inicializar_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                contraseña_hash TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

        insertar_usuario("Daniela", "clave1")
        insertar_usuario("Guillermo", "clave2")
        insertar_usuario("Cristhian", "clave3")
        insertar_usuario("Deyvi", "clave4")

def insertar_usuario(nombre, contraseña_clara):
    hash_pass = hashlib.sha256(contraseña_clara.encode()).hexdigest()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, contraseña_hash) VALUES (?, ?)", (nombre, hash_pass))
    conn.commit()
    conn.close()

def validar_usuario(nombre, contraseña_clara):
    hash_pass = hashlib.sha256(contraseña_clara.encode()).hexdigest()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña_hash = ?", (nombre, hash_pass))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']
        if validar_usuario(usuario, clave):
            return f"<h2>✅ Bienvenido, {usuario}</h2>"
        else:
            return "<h3>❌ Usuario o contraseña incorrecta</h3>"
    return '''
        <form method="post">
            Nombre de usuario: <input type="text" name="usuario"><br>
            Contraseña: <input type="password" name="clave"><br>
            <input type="submit" value="Ingresar">
        </form>
    '''

if __name__ == '__main__':
    inicializar_db()
    app.run(host='0.0.0.0', port=5800)
