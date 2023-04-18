from flask import Flask, render_template

app = Flask("__name__", static_folder="./static", template_folder="./templates")

@app.route("/")
def Index():
    return render_template("Home.Index.html")

@app.route("/Contato")
def Contato():
    return render_template("Contato.html")

@app.route("/Quem.Somos")
def QuemSomos():
    return render_template("Quem.Somos.html")

if __name__ == "__main__":
    app.run(debug=True) 