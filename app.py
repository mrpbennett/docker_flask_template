from flask import Flask, render_template, flash, redirect, url_for
from forms import SignUpForm, LoginForm

app = Flask(__name__)

app.config.from_object("config.DevConfig")


@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def second_page():
    return render_template("about.html", title="Second Page")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("signup.html", title="Sign Up", form=form)


# HTTP Error handlers ---
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
