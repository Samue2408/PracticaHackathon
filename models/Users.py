from config.db import app, db, ma

class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(100), unique= True)
    user = db.Column(db.String(100), unique= True)
    password = db.Column(db.String(100))
    mail = db.Column(db.String(150))
    phone = db.Column(db.Integer)
    profile_picture = db.Column(db.String(100))

    def __init__(self, name, user, password, mail, phone, profile_picture):
        self.name = name,
        self.user = user,
        self.password = password,
        self.mail = mail,
        self.phone = phone,
        self.profile_picture = profile_picture,

with app.app_context():
    db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user', 'password', 'mail', 'phone', 'profile_picture')