from flask import Blueprint, render_template, request

from .database import db
from .model import Item

bp = Blueprint('admin',__name__)

@bp.route('/admin')
def admin():
#    if request.method == 'POST':
#        name = request.form['shop_name']
#        if not Shop.query.filter(Shop.name == name).all():
#            shop = Shop(name = name)
#            db.session.add(shop)
#            db.session.commit()
#    shops = Shop.query.all()
    items = Item.query.all()

    return render_template('admin.html',items = items)