from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Quotes import Quotes, QuotesSchema
from models.Publications import Publications, PublicationSchema

ruta_quotes = Blueprint("ruta_quotes", __name__)

quote_schema = QuotesSchema()
quotes_schema = QuotesSchema(many=True)

@ruta_quotes.route("/quotes", methods=["GET"])
def quotes():
    resultall =  Quotes.query.all()
    result = quotes_schema.dump(resultall)
    session['quotes'] = result
    return result

@ruta_quotes.route("/saveQuotes", methods=["POST"])
def save_quotes():  
    publication_ = request.json['publication']
    publicacion_quote = request.json['publication_quotes']
    new_quote = Quotes(publication_, publicacion_quote)
    db.session.add(new_quote)
    db.session.commit()
    resultall = quotes_schema.dump(Quotes.query.all())
    session['quotes'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_quotes.route("/updateQuotes", methods=["PUT"])
def update_quotes():
    id = request.json["id"]
    nquotes = Quotes.query.get(id)
    nquotes.publication = request.json['publication']
    nquotes.publication_quotes = request.json['publication_quotes']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_quotes.route("/deleteQuotes/<id>", methods=["GET"])
def delete_quotes(id):
    quote = Quotes.query.get(id)
    db.session.delete(quote)
    db.session.commit()
    return jsonify(quote_schema.dump(quote))