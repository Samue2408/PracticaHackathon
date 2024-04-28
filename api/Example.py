from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Example import Example, ExampleSchema

ruta_Example = Blueprint("ruta_Example",__name__)

Example_schema = ExampleSchema()
Examplees_schema = ExampleSchema(many=True)

@ruta_Example.route("/Examplees", methods=["GET"])
def Examplees():
    resultall = Example.query.all()
    result = Examplees_schema.dump(resultall)    
    session['Examplees'] = result
    return redirect(url_for("ruta_jornada.jornadas"))

@ruta_Example.route("/saveExample", methods=["POST"])
def saveExample():
    name = request.json['name'].title()
    Example = db.session.query(Example.id).filter(Example.nombre == name).all()
    result = Examplees_schema.dump(Example)

    if len(result)==0:
        new_Example = Example(name)
        db.session.add(new_Example)
        db.session.commit()
        resultall = Example.query.all()
        result = Examplees_schema.dump(resultall)    
        session['Examplees'] = result
        return jsonify({'mensaje': 'Registro exitoso'}) 
    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401 
        
@ruta_Example.route("/updateExample", methods=["PUT"])
def updateExample():
    id = request.json['id']
    nExample = Example.query.get(id) #Select * from Cliente where id = id
    nExample.nombre = request.json['name'].title()
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_Example.route("/deleteExample/<id>", methods=["GET"])
def deleteExample(id):
    Example = Example.query.get(id)
    db.session.delete(Example)
    db.session.commit()
    return jsonify(Example_schema.dump(Example))