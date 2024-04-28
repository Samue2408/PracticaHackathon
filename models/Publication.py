from config.db import app, db, ma
from datetime import datetime

class Publications(db.Model):
    __tablename__ = "Publications"

    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))
    date_time = db.Column(db.DateTime, default=datetime.utctimetuple)
    message = db.Column(db.String(200))
    likes = db.Column(db.Integer)
    cita = db.Column(db.Boolean)    

    def __init__(self, id_user, date_time, message, likes, cita):
        self.id_user = id_user
        self.date_time = date_time
        self.message = message
        self.likes = likes
        self.cita = cita

with app.app_context():
    db.create_all()

class PublicationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_user', 'date_time', 'message', 'likes', 'cita')