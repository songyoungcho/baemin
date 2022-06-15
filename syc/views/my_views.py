from flask import Blueprint, url_for, render_template, flash, request, session, g

from werkzeug.utils import redirect

from syc import db
from syc.forms import StoreCreateForm
from syc.models import Store

bp = Blueprint('my', __name__, url_prefix='/my')


@bp.route('/my_page/', methods=('GET', 'POST'))
def my_page():
    return render_template('my/my.html')


@bp.route('/create_store/', methods=('GET', 'POST'))
def create_store():
    form = StoreCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        store = Store.query.filter_by(store_name=form.store_name.data).first()
        if not store:
            store = Store(store_name=form.store_name.data,
                          s_phone=form.s_phone.data,
                          s_address=form.s_address.data,
                          store_intro=form.store_intro.data,
                          min_order=form.min_order.data,
                          deliver=form.deliver.data, )
            db.session.add(store)
            db.session.commit()
            return redirect(url_for('main.main'))
        else:
            flash('이미 존재하는 가게입니다.')
    return render_template('my/create_store.html', form=form)
