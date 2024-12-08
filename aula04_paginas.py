from flask import Flask, render_template

app_gabriel = Flask(__name__ , template_folder='templates')

@app_gabriel.route("/")  
def homepage():
    return render_template ("homepage.html")

@app_gabriel.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__": 
     app_gabriel.run(port = 8000) 
                                