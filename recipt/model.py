from datetime import datetime
from recipt.database import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,default=datetime.now())
    shop_id = db.Column(db.Integer)
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    discount = db.Column(db.Integer,default=0)

    def __repr__(self) -> str:
        return f'<Item id:{self.id} date:{self.date} shop_id:{self.shop_id} name:{self.name} price:{self.price} discount:{self.discount}>'