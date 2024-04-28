from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Retweets import Retweets, RetweetsShema

ruta_retweets = Blueprint("ruta_retweets", __name__)

retweet_schema = RetweetsShema()
retweets_schema = RetweetsShema(many=True)

@ruta_retweets.route("/retweets", methods=["GET"])
def retweets():
    resultall =  Retweets.query.all()
    result = retweets_schema.dump(resultall)
    session['retweets'] = result
    return redirect(url_for("retweets"))

@ruta_retweets.route("/saveRetweets", methods=["POST"])
def save_retweets():  
    date_time = request.json['date_time']
    user = request.json['user']
    publication = request.json['publication']
    quotes = request.json['quotes']
    new_retweets = Retweets(date_time = date_time, user = user, publication = publication, quotes = quotes)
    db.session.add(new_retweets)
    db.session.commit()
    resultall = Retweets.query.all()
    session['retweets'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_retweets.route("/updateRetweets", methods=["PUT"])
def update_retweets():
    id = request.json["id"]
    nRetweet = Retweets.query.get(id)
    nRetweet.date_time = request.json['date_time']
    nRetweet.user = request.json['user']
    nRetweet.publication = request.json['publication']
    nRetweet.quotes = request.json['quotes']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_retweets.route("/deleteRetweets/<id>", methods=["GET"])
def delete_retweets(id):
    retweet = Retweets.query.get(id)
    db.session.delete(Retweets)
    db.session.commit()
    return jsonify(retweet_schema.dump(retweet))