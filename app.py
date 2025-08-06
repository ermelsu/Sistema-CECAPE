from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "segredo_super_seguro"

def get_db_connection():
    conn = sqlite3.connect('database/usuarios.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,)).fetchone()
        conn.close()
        if user and check_password_hash(user['senha'], senha):
            session['usuario'] = user['nome']
            session['tipo'] = user['tipo']
            return redirect('/landing')
        return "Login inválido!"
    return render_template('login.html')

@app.route('/landing')
def landing():
    if 'usuario' not in session:
        return redirect('/')
    return render_template('landingPage.html', usuario=session['usuario'], tipo=session['tipo'])


@app.route('/solicitacoes')
def solicitacoes():
    if 'usuario' not in session:
        return redirect('/')
    return render_template('solicitacao.html', usuario=session['usuario'], tipo=session['tipo'])


@app.route('/produtos')
def produtos():
    if 'usuario' not in session:
        return redirect('/')
    return render_template('produtos.html', usuario=session['usuario'], tipo=session['tipo'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
