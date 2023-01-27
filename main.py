from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template(
        "index.html",
        page_title="Page d'accueil"
    )


@app.route("/contact/")
def contact_page():
	return render_template("pages/contact.html")


@app.route("/support/")
def support_page():
    return render_template("pages/support.html")


if __name__ == "__main__":
    app.run()

