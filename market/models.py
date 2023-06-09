from market import db

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Item {self.name}' #super().__repr__()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1500)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self) -> str:
        return f'User {self.username}'

