import datetime
from flask import Blueprint, render_template, request

from .database import db
from .model import Item,Shop

bp = Blueprint('item',__name__)

@bp.route('/item/<int:shop_id>', methods=('GET','POST'))
def register(shop_id):

    if request.method == 'POST':
        date = datetime.date.fromisoformat(request.form['date']) if request.form['date'] else datetime.date.today()        
        names = request.form.getlist('name')
        prices = request.form.getlist('price')
        discounts = request.form.getlist('discount')
        for i in range(len(names)):
            if names[i]:
                item = Item(date = date, shop_id=shop_id, name = names[i], price = prices[i], discount=discounts[i])
                db.session.add(item)
        db.session.commit()
    shop = Shop.query.filter(Shop.id == shop_id).one_or_none()

    return render_template('item.html',shop_name = shop.name)