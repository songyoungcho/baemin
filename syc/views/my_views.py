from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from syc import db
from syc.models import User

bp=Blueprint('my',__name__,url_prefix='/my')

@bp.route('/mypage/', methods=('GET','POST'))
def mypage():
    return render_template('mine/my.html')