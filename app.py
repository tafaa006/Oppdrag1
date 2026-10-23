from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/om_oss")
def om_oss():
    return render_template("om_oss.html")

@app.route("/filmer")
def filmer():
    return render_template("Filmer.html")

@app.route("/bestilling", methods=["GET", "POST"])
def bestilling():
    if request.method == "POST":
        navn = request.form.get("navn", "").strip()
        film = request.form.get("film", "")
        aldersgruppe = request.form.get("aldersgruppe", "")
        dato = request.form.get("dato", "")
        visningstid = request.form.get("visningstid", "")
        antall = request.form.get("antall", "")

        return render_template(
            "bekreftelse.html",
            navn=navn,
            film=film,
            aldersgruppe=aldersgruppe,
            dato=dato,
            visningstid=visningstid,
            antall=antall,
        )

    return render_template("bestilling.html")

if __name__ == "__main__":
    app.run(debug=True)