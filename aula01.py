from flask import Flask

app_gabriel = Flask (__name__)

@app_gabriel.route('/')
def raiz():
    return 'Olá, turma!'

app_gabriel.run()
