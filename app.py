from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Olá ... seja bem vindo a lambda publicado com o Zappa"


@app.route("/users", methods = ['POST'])
def create_user():
    return request.json


if __name__ == '__main__':
    app.run()
