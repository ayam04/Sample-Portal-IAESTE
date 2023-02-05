from flask import Flask, render_template, request

app = Flask(__name__)

offers = [
    {
        "title": "Intern",
        "time": "2 month",
        "country": "Tunisia"
    },
    {
        "title": "Intern",
        "time": "3months",
        "country": "UAE"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@iaeste.com" and password == "pswd":
            action = request.form["action"]
            if action == "show":
                return render_template("offers.html", offers=offers)
            elif action == "add":
                return render_template("add_offer.html")
        else:
            return "Incorrect email or password"
    return render_template("login.html")

@app.route("/add_offer", methods=["POST"])
def add_offer():
    offer_title = request.form["offer_title"]
    offer_time = request.form["offer_time"]
    offer_country = request.form["offer_country"]

    offers.append({
        "title": offer_title,
        "time": offer_time,
        "country": offer_country
    })

    return render_template("offers.html", offers=offers)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)