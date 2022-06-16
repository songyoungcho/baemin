from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField,DateTimeField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired('이름은 필수입력 항목입니다.'), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    phone = StringField('전화번호', validators=[DataRequired(), Length(min=11, max=11)])
    address = StringField('주소', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class StoreCreateForm(FlaskForm):
    store_name = StringField('가게이름', validators=[DataRequired(), Length(min=1, max=25)])
    s_phone = StringField('전화번호', validators=[DataRequired(), Length(min=10, max=11)])
    s_address = StringField('주소', validators=[DataRequired()])
    store_intro = TextAreaField('가게 설명', validators=[DataRequired()])
    min_order = StringField('주문 최소 금액', validators=[DataRequired()])
    deliver = StringField('배달료', validators=[DataRequired()])

class MenuCreateForm(FlaskForm):
    menu_name = StringField('메뉴이름', validators=[DataRequired(), Length(min=1, max=25)])
    price = StringField('가격', validators=[DataRequired()])
    menu_content = TextAreaField('메뉴 설명', validators=[DataRequired()])