from flask import Flask, render_template

app = Flask(__name__)


# criar a 1ª pagina do site
# route -> sitejv.com/
# funçâo -> o que você quer exibir naquela página
# template


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/trends")
def trends():
    return render_template("trends.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)






