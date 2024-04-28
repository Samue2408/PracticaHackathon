from config.db import app, db, ma
from datetime import datetime

class retweets(db.model):
    __tablename__ = "Retweet"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    date_time = db.Column(db.DateTime, default=datetime.utctimetuple)
    user = db.Column(db.Integer, db.foreignKey("Users.id"))
    publication = db.Column(db.Integer, db.foreignKey("Publications.id"))
    quotes = db.Column(db.Integer, db.ForeignKey("Quotes.id"))
    
    
    def __init__(self, id, date_time, user, publication, quotes):
        self.id = id
        self.date_time = date_time
        self.user = user
        self.publication = publication
        self.quotes = quotes  
        
with app.app_context():
    db.create_all()


class RetweetsShema(ma.Schema):
    class Meta:
        fields = ('id','date', 'users', 'publication', 'quotes')