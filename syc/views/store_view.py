from flask import Blueprint, url_for, render_template, flash, request, session, g

from werkzeug.utils import redirect

from syc import db
from syc.models import Store, Menu, User

bp = Blueprint('store', __name__, url_prefix='/store')


@bp.route('/list/korean/')
def _list1():
    store_list = Store.query.filter(Store.store_type.like('한식')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/chinese/')
def _list2():
    store_list = Store.query.filter(Store.store_type.like('중식')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/japanese/')
def _list3():
    store_list = Store.query.filter(Store.store_type.like('일식')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/snack/')
def _list4():
    store_list = Store.query.filter(Store.store_type.like('분식')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/asian/')
def _list5():
    store_list = Store.query.filter(Store.store_type.like('아시안')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/chicken/')
def _list6():
    store_list = Store.query.filter(Store.store_type.like('치킨')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/pizza/')
def _list7():
    store_list = Store.query.filter(Store.store_type.like('피자')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/lunch/')
def _list8():
    store_list = Store.query.filter(Store.store_type.like('도시락')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/pork/')
def _list9():
    store_list = Store.query.filter(Store.store_type.like('족발')).all()
    return render_template('store/store_list.html', store_list=store_list)
@bp.route('/list/desert/')
def _list10():
    store_list = Store.query.filter(Store.store_type.like('디저트')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/fast/')
def _list11():
    store_list = Store.query.filter(Store.store_type.like('패스트푸드')).all()
    return render_template('store/store_list.html', store_list=store_list)

@bp.route('/list/dawn/')
def _list12():
    store_list = Store.query.filter(Store.store_type.like('야식')).all()
    return render_template('store/store_list.html', store_list=store_list)





@bp.route('/detail/<int:store_id>/')
def detail(store_id):
    store = Store.query.get_or_404(store_id)
    return render_template('store/store_detail.html', store=store)

