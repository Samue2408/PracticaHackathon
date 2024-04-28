from flask import Blueprint, jsonify, request, json, redirect, url_for, session
from config.db import db, app, ma
from models.Publications import Publications, PublicationSchema

ruta_publications = Blueprint("ruta_ruta",__name__)

publication_schema = PublicationSchema()
publications_schema = PublicationSchema(many=True)

@ruta_publications.route("/Publications", methods=["GET"])
def Publication():
    resultall = Publications.query.all()
    result = publications_schema.dump(resultall)    
    session['publications'] = result
    return result

@ruta_publications.route("/savePublication", methods=["POST"])
def savePublication():
    id_user = request.json['id_user']
    message = request.json['message']
    likes = request.json['likes']
    quotes = request.json['phone']
    new_publication = Publications(id_user= id_user, message= message, likes= likes, quotes= quotes)
    db.session.add(new_publication)
    db.session.commit()
    resultall = Publications.query.all()
    result = publications_schema.dump(resultall)  
    session['publications'] = result
    return jsonify({'mensaje': 'Registro exitoso'}) 
        
@ruta_publications.route("/updatePublication", methods=["PUT"])
def updatePublication():
    id = request.json['id']
    nPublication = Publications.query.get(id) #Select * from Cliente where id = id
    nPublication.id_user = request.json['id_user']
    nPublication.message = request.json['message']
    nPublication.likes = request.json['likes']
    nPublication.quotes = request.json['phone']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_publications.route("/deletePublication/<id>", methods=["GET"])
def deletePublication(id):
    publication = Publications.query.get(id)
    db.session.delete(publication)
    db.session.commit()
    return jsonify(publication_schema.dump(publication))