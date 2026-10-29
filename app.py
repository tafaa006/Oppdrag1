from flask import Flask, render_template, request

app = Flask(__name__)

pris = 120;

setene = [
    {"id": 1, "navn": "budsjett", "multi": 0.8},
    {"id": 2, "navn": "normal", "multi": 1},
    {"id": 3, "navn": "luksus", "multi": 1.2},
]


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
        seter = request.form.get("seter", "")
        visningstid = request.form.get("visningstid", "")
        antall = request.form.get("antall", "")
        kommentar = request.form.get("kommentar", "").strip()

        for sete in setene:
            if str(sete["id"]) == seter:
                seter = sete["navn"]
                break

        total_pris = pris * sete["multi"] * int(antall)

        if kommentar == "":
            kommentar = "ingenting"

        return render_template(
            "bekreftelse.html",
            navn=navn,
            film=film,
            seter=seter,
            aldersgruppe=aldersgruppe,
            dato=dato,
            visningstid=visningstid,
            antall=antall,
            kommentar=kommentar,
            total_pris=total_pris,
        )

    return render_template("bestilling.html", setene=setene)

if __name__ == "__main__":
    app.run(debug=True)