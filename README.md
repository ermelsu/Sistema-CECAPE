
# 📦 Sistema de Requisição - CECAPE

Sistema web para requisição de materiais desenvolvido para otimizar a comunicação entre os setores administrativos e o almoxarifado do CECAPE.

---

## 🚀 Funcionalidades

- ✅ Login com autenticação via Google Planilhas (usuários pré-cadastrados)
- 🧾 Cadastro e envio de requisições de materiais
- 🛠️ Tela administrativa com acompanhamento e alteração de status dos pedidos
- 🕓 Histórico de requisições por usuário
- 📄 Integração com planilhas Google para armazenamento e controle
- 📊 Interface amigável para visualização e filtragem dos dados

---

## 🧠 Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Deploy:** Heroku / GitHub Pages
- **Banco de Dados:** Google Sheets (como base de usuários e materiais)
- **Controle de Versão:** Git e GitHub

---

## ⚙️ Como executar localmente

1. Clone este repositório:

```bash
git clone https://github.com/ermelsu/Sistema-CECAPE.git
cd Sistema-CECAPE
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o sistema:

```bash
python app.py
```

> Em produção, o Heroku utilizará o Gunicorn como especificado no `Procfile`.

---

## 🖼️ Estrutura do Projeto

```
📁 database/       # Base de dados locais (opcional)
📁 static/         # Arquivos estáticos (CSS, JS, imagens)
📁 templates/      # Templates HTML com Jinja2
📄 app.py          # Arquivo principal da aplicação Flask
📄 requirements.txt
📄 runtime.txt
📄 Procfile
```

---

## 📌 Observações

- O sistema ainda está em desenvolvimento e novas funcionalidades podem ser adicionadas.
- Para usar autenticação com planilhas Google, configure corretamente suas credenciais no projeto (detalhes omitidos por segurança).

---

## 👨‍💻 Autor

Desenvolvido com ❤️ por [Emerson Silva](https://github.com/ermelsu)

---

## 🏫 Projeto interno da faculdade CECAPE

Este projeto é de uso institucional e visa melhorar o fluxo de trabalho entre setores administrativos e o almoxarifado.
