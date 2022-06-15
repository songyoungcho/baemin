from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from syc import db
from syc.forms import UserCreateForm, UserLoginForm
from syc.models import User

bp=Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def main():
    return render_template('main.html')