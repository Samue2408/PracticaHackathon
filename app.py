from flask import Flask, render_template, request, redirect, url_for, session, make_response
from config.db import app, db

from api.Example import ruta_Example

app.register_blueprint(ruta_Example, url_prefix="/api")

@app.route("/")
def index():
    return render_template('login.html')
