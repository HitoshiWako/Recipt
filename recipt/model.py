from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from recipt.database import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,default=datetime.now())
    shop_id = db.Column(db.Integer, ForeignKey('shops.id'))
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    discount = db.Column(db.Integer,default=0)
    shop = relationship('Shop')

    def __repr__(self) -> str:
        return f'<Item id:{self.id} date:{self.date} shop_id:{self.shop_id} name:{self.name} price:{self.price} discount:{self.discount}>'

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    items = relationship('Item', uselist=True)

    def __repr__(self) -> str:
        return f'<Shop id:{self.id} name:{self.name}>'