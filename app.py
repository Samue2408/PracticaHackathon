from flask import Flask, render_template, request, redirect, url_for, session, make_response
from config.db import app, db

from api.Example import ruta_Example
from api.Users import ruta_users
from api.Publications import ruta_publications
from api.Quotes import ruta_quotes
from api.Retweets import ruta_retweets

app.register_blueprint(ruta_Example, url_prefix="/api")
app.register_blueprint(ruta_users, url_prefix="/api/users")
app.register_blueprint(ruta_publications, url_prefix="/api/publications")
app.register_blueprint(ruta_retweets, url_prefix="/api/retweets")
app.register_blueprint(ruta_quotes, url_prefix="/api/quotes")

@app.route("/")
def index():
    return render_template('login.html')

if __name__ == '__main__': 
    app.run(debug=True, port=5000)