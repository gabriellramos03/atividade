from flask import Flask, render_template

app_gabriel = Flask(__name__, template_folder='t_templates') 
@app_gabriel.route("/")
@app_gabriel.route("/index")  
def indice():
    return render_template ("t_index.html")

@app_gabriel.route("/contato")
def contato():
    return render_template("t_contato.html") 

@app_gabriel.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""}) 
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

if __name__ == "__main__": 
     app_gabriel.run(port = 8000) 
     