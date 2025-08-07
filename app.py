# ZONA 0: Conexão com o banco
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database/usuarios.db')  # Altere se o nome do banco for outro
    conn.row_factory = sqlite3.Row
    return conn
# ========================================
# ZONA 1: IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# ========================================
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Caminho do banco de dados
DATABASE = 'database/usuarios.db'

def conectar_banco():
    return sqlite3.connect(DATABASE)

# ========================================
# ZONA 2: ROTAS DE AUTENTICAÇÃO
# ========================================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[3], senha):
            session['usuario'] = user[2]
            session['tipo'] = user[4]
            return redirect(url_for('landing'))
        else:
            return render_template('login.html', erro=True)

    return render_template('login.html', erro=False)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ========================================
# ZONA 3: ROTAS PRINCIPAIS
# ========================================
@app.route('/landing')
def landing():
    return render_template('landingpage.html')

@app.route('/solicitacoes')
def solicitacoes():
    return render_template('solicitacoes.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']
        tipo = request.form['tipo']

        senha_hash = generate_password_hash(senha)

        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, usuario, senha, tipo) VALUES (?, ?, ?, ?)",
                       (nome, usuario, senha_hash, tipo))
        conn.commit()
        conn.close()

        return redirect(url_for('usuarios'))

    return render_template('cadastro.html')

# ========================================
# ZONA 4: USUÁRIOS - LISTAR, EDITAR, DELETAR
# ========================================
# ZONA 4: Rota de gerenciamento de usuários
@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Deletar usuário
    if request.method == 'POST' and 'deletar_id' in request.form:
        id = request.form['deletar_id']
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
        conn.commit()

    # Editar usuário
    elif request.method == 'GET' and 'editar' in request.args:
        id = request.args.get('editar')
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
        editar = cursor.fetchone()
    else:
        editar = None

    # Cadastrar ou atualizar usuário
    if request.method == 'POST' and 'nome' in request.form:
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']
        tipo = request.form['tipo']

        if 'editar_id' in request.form:
            id = request.form['editar_id']
            cursor.execute('''
                UPDATE usuarios SET nome=?, usuario=?, senha=?, tipo=? WHERE id=?
            ''', (nome, usuario, senha, tipo, id))
        else:
            cursor.execute('''
                INSERT INTO usuarios (nome, usuario, senha, tipo)
                VALUES (?, ?, ?, ?)
            ''', (nome, usuario, senha, tipo))
        conn.commit()

    # Agora sim: pegar todos os usuários para exibir
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    conn.close()
    return render_template('usuarios.html', usuarios=usuarios, editar=editar)

# ========================================
# ZONA 5: EXECUÇÃO
# ========================================
if __name__ == '__main__':
    app.run()
