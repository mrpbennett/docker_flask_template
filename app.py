from flask import Flask, render_template

app = Flask(__name__)

""" 
When you're ready to set to PROD replace config.DevConfig with config.ProdConfig
like so: app.config.from_object('config.ProdConfig')
"""

app.config.from_object("config.DevConfig")


@app.route("/")
def function_name():
    return render_template("home.html")


# HTTP Error handlers ---
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
