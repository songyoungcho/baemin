from syc import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_store = db.Column(db.Boolean(), default=False, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=True)
    address = db.Column(db.String(200), nullable=True)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(150), unique=True, nullable=False)
    store_type = db.Column(db.String(150), default="한식", nullable=False)
    s_phone = db.Column(db.String(120), unique=True, nullable=False)
    s_address = db.Column(db.String(200), nullable=False)
    store_intro = db.Column(db.Text(),nullable=True)
    min_order = db.Column(db.Integer, nullable=False)
    deliver = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('store_set'))

class Menu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    store_id=db.Column(db.Integer,db.ForeignKey('store.id',ondelete='CASCADE'))  #ondelete-> 질문을 삭제하면 답변도 같이 삭제됨.
    # 질문 삭제 시 question_id만 빈값이 아닌 모든 데이터 삭제하려면
    # question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    menu_name = db.Column(db.String(150), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    menu_content=db.Column(db.Text(),nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False, default=1)
    user = db.relationship('User', backref=db.backref('menu_set'))