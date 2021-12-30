from datetime import datetime
from recipt.database import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,default=datetime.now())
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f'<Item id:{self.id} date:{self.date} name:{self.name} price:{self.price}>'