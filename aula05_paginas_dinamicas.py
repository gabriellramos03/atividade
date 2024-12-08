from flask import Flask, render_template

app_gabriel = Flask(__name__ , template_folder='templates')

@app_gabriel.route("/") 
def homepage():  
    return render_template ("homepage.html")

@app_gabriel.route("/contato")
def contato():
    return render_template("contato.html") 

@app_gabriel.route("/index")
def indice():
    return render_template ("index.html") 

@app_gabriel.route("/usuario")
def dados_usuario():
    nome_usuario="Mariela"
    dados_usu = {"profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)
                                        
if __name__ == "__main__": 
     app_gabriel.run(port = 8000) 
                                