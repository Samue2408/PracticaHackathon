from flask import Blueprint, jsonify, request, json, redirect, url_for, session
from config.db import db, app, ma
from models.Users import Users, UserSchema

ruta_users = Blueprint("ruta_users",__name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@ruta_users.route("/Users", methods=["GET"])
def User():
    resultall = Users.query.all()
    result = users_schema.dump(resultall)    
    session['users'] = result
    return result

@ruta_users.route("/saveUser", methods=["POST"])
def saveUser():
    name = request.json['name'].title()
    User = db.session.query(Users.id).filter(Users.name == name).all()
    result = users_schema.dump(User)

    if len(result)==0:
        user = request.json['user']
        password = request.json['password']
        mail = request.json['mail']
        phone = request.json['phone']
        profile_picture = request.json['profile_picture']
        new_User = Users(name, user, password, mail, phone, profile_picture)
        db.session.add(new_User)
        db.session.commit()
        resultall = Users.query.all()
        result = users_schema.dump(resultall)  
        session['users'] = result
        return jsonify({'mensaje': 'Registro exitoso'}) 
    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401 
        
@ruta_users.route("/updateUsers", methods=["PUT"])
def updateUsers():
    id = request.json['id']
    nUser = Users.query.get(id) #Select * from Cliente where id = id
    nUser.name = request.json['name'].title()
    nUser.user = request.json['user']
    nUser.password = request.json['password']
    nUser.mail = request.json['mail']
    nUser.phone = request.json['phone']
    nUser.profile_picture = request.json['profile_picture']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_users.route("/deleteUser/<id>", methods=["GET"])
def deleteUser(id):
    User = Users.query.get(id)
    db.session.delete(User)
    db.session.commit()
    return jsonify(user_schema.dump(User))