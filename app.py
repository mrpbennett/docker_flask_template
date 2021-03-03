from flask import Flask, render_template
import settings
import secrets

# generate a secret key via secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key

@app.route("/")
def function_name():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

