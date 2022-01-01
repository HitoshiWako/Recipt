from flask import Blueprint, render_template, request

from .database import db
from .model import Item

bp = Blueprint('admin',__name__)

@bp.route('/admin', methods=('GET','POST'))
def admin():

    if request.method == 'POST':
        id = request.form['delete']
        Item.query.filter(Item.id==id).delete()
        db.session.commit()
    items = Item.query.all()

    return render_template('admin.html',items = items)