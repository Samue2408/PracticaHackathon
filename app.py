from flask import Flask, render_template, request, redirect, url_for, session, make_response
from config.db import app, db

from api.Example import ruta_Example

app.register_blueprint(ruta_Example, url_prefix="/api")

@app.route("/")
def index():
    return render_template('login.html')


if __name__ == '__main__': 
    app.run(debug=True, port=5000)