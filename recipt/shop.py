from flask import Blueprint, render_template, request

from .database import db
from .model import Shop

bp = Blueprint('shop',__name__)

@bp.route('/shop',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        name = request.form['shop_name']
        if not Shop.query.filter(Shop.name == name).all():
            shop = Shop(name = name)
            db.session.add(shop)
            db.session.commit()
    shops = Shop.query.all()
    return render_template('shop.html',shops=shops)