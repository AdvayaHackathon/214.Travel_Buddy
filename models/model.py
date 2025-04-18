from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(30),nullable=False,unique=True)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(50),nullable=False)
    phone_number=db.Column(db.String(10),nullable=False)
    use=db.relationship("Posts",backref="usersi")
    city=db.Column(db.String,nullable=False)


class Cities(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    country=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String(100),nullable=True)
    cit=db.relationship("Places",backref="citi")


class Places(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    cit_id=db.Column(db.Integer,db.ForeignKey("cities.id"))
    rating=db.Column(db.Float,nullable=False)


class Communities(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String(100),nullable=True)
    commu=db.relationship("Posts",backref="communi")


class Posts(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    community_id=db.Column(db.Integer,db.ForeignKey("communities.id"))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    content=db.Column(db.String(100),nullable=False)
