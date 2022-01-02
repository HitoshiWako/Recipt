from flask import Blueprint, render_template, request

from .database import db
from .model import Item,Shop

bp = Blueprint('item',__name__)

@bp.route('/item/<int:shop_id>', methods=('GET','POST'))
def register(shop_id):

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        discount = request.form['discount']
        item = Item(shop_id=shop_id, name=name, price=price, discount=discount)
        db.session.add(item)
        db.session.commit()
    shop = Shop.query.filter(Shop.id == shop_id).one_or_none()

    return render_template('item.html',shop_name = shop.name)