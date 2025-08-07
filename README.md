
# GECAPE - Sistema de Gestão de Materiais do CECAPE

O **GECAPE** (Gestão de Estoque do CECAPE) é um sistema completo para **requisição, controle e administração de materiais** do almoxarifado da instituição. Desenvolvido com foco em clareza, acessibilidade e organização, o sistema visa **otimizar o fluxo de trabalho**, centralizar informações e facilitar tomadas de decisão.

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** – Framework web simples e poderoso
- **Jinja2** – Templates dinâmicos HTML
- **SQLite** – Banco de dados local e leve
- **Bootstrap + CSS customizado** – Interface amigável e responsiva
- **Font Awesome** – Ícones modernos
- **Heroku** – Deploy automático e escalável

## 📦 Funcionalidades

- 🔐 **Login Seguro** com autenticação de usuários
- 👥 **Cadastro de usuários**
- 🧾 **Solicitação de materiais** com formulário dinâmico
- 📄 **Visualização e controle de requisições**
- 📊 **Painel administrativo** para acompanhamento de status
- 🗂️ Interface dividida entre usuários e administradores
- ☁️ **Deploy em nuvem com Heroku**

## 🗂️ Organização do Projeto

```bash
GECAPE/
│
├── static/
│   ├── css/
│   ├── img/
│   └── js/
│
├── templates/
│   ├── login.html
│   ├── usuarios.html
│   ├── solicitacoes.html
│   └── base.html
│
├── app.py
├── requirements.txt
├── Procfile
└── README.md
```

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seuusuario/GECAPE.git
cd GECAPE

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
```

Acesse `http://localhost:5000` no seu navegador.

## ☁️ Deploy no Heroku

1. Faça login no Heroku CLI:
   ```bash
   heroku login
   ```

2. Crie um novo app:
   ```bash
   heroku create gecape
   ```

3. Faça o push:
   ```bash
   git push heroku main
   ```

4. Acesse:
   ```
   https://gecape.herokuapp.com/
   ```

## 👤 Desenvolvido por

**Emerson Silva Bezerra**  
Responsável pelo Almoxarifado | Faculdade CECAPE  
💡 Apaixonado por automação, design limpo e sistemas funcionais.

---

**GECAPE** é mais que um sistema. É o futuro da gestão de materiais no CECAPE.
