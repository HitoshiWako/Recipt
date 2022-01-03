from flask import Blueprint, render_template, request
from sqlalchemy import desc

from .database import db
from .model import Item, Shop

bp = Blueprint('main',__name__)

@bp.route('/', methods=('GET','POST'))
def index():
    items = Item.query.order_by(desc(Item.date)).limit(20).all()
    shops = Shop.query.all()
    return render_template('index.html',items = items, shops = shops)