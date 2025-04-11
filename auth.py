from flask import Blueprint, request, render_template, redirect, session
from models.model import *
bp = Blueprint('auth', __name__)
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
            return redirect(f"/dashboard/{user.id}")
    return render_template("login.html")


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    # In a real app, save to DB
    username = request.form.get('username')
    password = request.form.get('password')
    session['user_id'] = 2
    return redirect('/banner')


@bp.route('/banner')
def banner():
    return render_template('banner.html')

@bp.route('/community')
def community():
    city = request.args.get('city', 'Unknown')
    return render_template('community.html', city=city)

@bp.route('/chat')
def chat():
    group = request.args.get('group', 'General')
    return render_template('chat.html', group=group)

@bp.route('/place')
def place():
    return render_template('place_details.html')