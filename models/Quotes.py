from config.db import db, app, ma


class Quotes(db.Model):
    __tablename__ = "Quotes"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    publication = db.Column(db.Integer, db.ForeignKey('Publications.id'))
    publication_quotes = db.Column(db.Integer, db.ForeignKey('Publications.id'))
    
    def __init__(self, publication, publication_quotes):
        self.publication = publication
        self.publication_quotes = publication_quotes

with app.app_context():
    db.create_all()
    
class QuotesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'publication', 'publication_quotes')