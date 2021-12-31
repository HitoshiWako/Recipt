from flask import Blueprint,render_template

bp = Blueprint('shop',__name__)

@bp.route('/shop',methods=('GET','POST'))
def register():
    return render_template('shop.html')