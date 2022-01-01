from flask import Blueprint,render_template
from .model import Shop

bp = Blueprint('shop',__name__)

@bp.route('/shop',methods=('GET','POST'))
def register():
    shops = Shop.query.all()
    return render_template('shop.html',shops=shops)