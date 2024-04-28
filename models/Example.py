from config.db import app, db, ma

class Example(db.Model):
    __tablename__ = "Examples"

    codigo = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), unique= True)

    def __init__(self, name):
        self.nombre = name

with app.app_context():
    db.create_all()

class ExampleSchema(ma.Schema):
    class Meta:
        fields = ('codigo', 'nombre')