from flask import Blueprint, url_for, request,render_template,g
from werkzeug.utils import redirect

from syc import db
from syc.forms import MenuCreateForm
from syc.models import User, Menu,Store
from .auth_views import login_required

bp = Blueprint('menu', __name__, url_prefix='/menu')


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