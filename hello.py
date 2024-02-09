# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>Nicolas Freitas Silveira</td></tr><tr><td><b>Prontuário:</b></td><td>PT3019144</td></tr></table>'
