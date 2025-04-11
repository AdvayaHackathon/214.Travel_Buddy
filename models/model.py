from flask import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(30),nullable=False,unique=True)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(50),nullable=False)
    use=db.relationship("Posts",backref="users")


class Cities(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    country=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String(100),nullale=True)
    cit=db.relationship("Places",backref="citi")


class Places(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    city_id=db.Column(db.Integer,db.Foreign_key("Cities.id"))
    name=db.Column(db.String(50),nullable=False)
    rating=db.Column(db.Float,nullable=False)


class Communities(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String(100),nullable=True)
    commu=db.relationship("Posts",backref="communi")


class Posts(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    user_id=db.Column(db.Integer,db.Foreign_key("user.id"))
    community_id=db.Column(db.Integer,db.Foreign_key("communities.id"))
    content=db.Column(db.String(100),nullable=False)
