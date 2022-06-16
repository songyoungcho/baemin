from flask import Blueprint, url_for, request,render_template,g, flash
from werkzeug.utils import redirect

from syc import db
from syc.forms import MenuCreateForm
from syc.models import User, Menu,Store
from .auth_views import login_required

bp = Blueprint('menu', __name__, url_prefix='/menu')
sum=0

@bp.route('/create_menu/<int:store_id>/', methods=('GET', 'POST'))
@login_required
def create_menu(store_id):
    form = MenuCreateForm()
    store = Store.query.get_or_404(store_id)
    if request.method == 'POST' and form.validate_on_submit():
        menu = Menu.query.filter_by(menu_name=form.menu_name.data).first()
        if not menu:
            menu = Menu(
                        menu_name=form.menu_name.data,
                        price=form.price.data,
                        menu_content=form.menu_content.data,
                        user=g.user)
            store.menu_set.append(menu)
            db.session.commit()
            return redirect(url_for('store.detail', store_id=store_id))
    return render_template('my/create_menu.html',  form=form)

@bp.route('/modify/<int:menu_id>', methods=('GET', 'POST'))
@login_required
def modify(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    if g.user != menu.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('store.detail', store_id=menu.store.id))
    if request.method == "POST":
        form = MenuCreateForm()
        if form.validate_on_submit():
            form.populate_obj(menu)
            db.session.commit()
            return redirect(url_for('store.detail', store_id=menu.store.id))
    else:
        form = MenuCreateForm(obj=menu)
    return render_template('my/create_menu.html', form=form)

@bp.route('/delete/<int:menu_id>')
@login_required
def delete(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    store_id = menu.store.id
    if g.user != menu.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(menu)
        db.session.commit()
    return redirect(url_for('store.detail', store_id=store_id))

@bp.route('/inbag/<int:sum>', methods=('GET', 'POST'))
# @bp.route('/inbag/<int:menu_id>/')
@login_required
def inbag(menu_id,price):

    _menu = Menu.query.get_or_404(menu_id)
    store_id = _menu.store.id
    if g.user == _menu.user:
        flash('본인가게 메뉴는 추가할 수 없습니다')
    else:
        _menu.buyer.append(g.user)
        db.session.commit()
    price=Menu.query.get_or_404(price)
    sum+=price
    return redirect(url_for('my/my', store_id=store_id, sum=sum))