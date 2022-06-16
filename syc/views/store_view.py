from flask import Blueprint, url_for, render_template, flash, request, session, g

from werkzeug.utils import redirect

from syc import db
from syc.models import Store, Menu, User

bp = Blueprint('store', __name__, url_prefix='/store')


@bp.route('/list/')
def _list():
    store_list = Store.query.filter(Store.store_type.like('한식')).all()
    return render_template('store/store_list.html', store_list=store_list)


@bp.route('/detail/<int:store_id>/')
def detail(store_id):
    store = Store.query.get_or_404(store_id)
    return render_template('store/store_detail.html', store=store)

