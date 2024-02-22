# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():

    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'


@app.route('/contextorequisicao')
def contexto_requisicao():

    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host

    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {user_agent}</h2><h2>O IP do computador remoto é: {remote_ip}</h2><h2>O host da aplicação é: {host}</h2><a href="/">Voltar</a>'