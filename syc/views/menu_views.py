from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from syc import db
from syc.models import User, Menu,Store

bp = Blueprint('menu', __name__, url_prefix='/menu')


@bp.route('/create/<int:store_id>', methods=('POST',))
def create(store_id):
    store = Store.query.get_or_404(store_id)
    menu_name = request.form['menu_name']
    price = request.form['price']
    menu_content = request.form['menu_content']
    menu = Menu(store_id=store, menu_name=menu_name, price=price, menu_content=menu_content)
    db.session.add(menu)
    db.session.commit()
    return redirect(url_for('store.detail', store_id=store_id))