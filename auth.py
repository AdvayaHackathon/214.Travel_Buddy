from flask import Blueprint, request, render_template, redirect, session
from models.model import *
bp = Blueprint('auth', __name__)
city_id=[1,2,3]
cities={"chennai":{1:"Fairlands",2:"Marketplace",3:"3 roads",4:"4 roads",5:"old bus stand",6:"new bustand"}}
@bp.route('/')
def home():
    return render_template('login.html')


@bp.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter(User.username == username).first()
        if user and user.password == password:
            session["user_id"] = user.id
            return redirect(f"/{user.id}/banner")
    return render_template("login.html")


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    # In a real app, save to DB
    username = request.form.get('username')
    password = request.form.get('password')
    session['user_id'] = 2
    return redirect(f'/banner')


@bp.route('/banner',methods=["GET"])
def banner():
    return render_template('banner.html',data=cities)


@bp.route('/communitylobby')
def communitylobby():
    return render_template("communitylobby.html",data=cities["chennai"])