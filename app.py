from flask import Flask,render_template,redirect,session,request
from models.model import *
app = Flask(__name__)
app.config['SECRET_KEY']='East'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///TravelBuddy.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
with app.app_context():
    db.create_all()

city_id=[1,2,3]
cities={"chennai":{1:"Fairlands",2:"Marketplace",3:"3 roads",4:"4 roads",5:"old bus stand",6:"new bustand"}}
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter(User.username == username).first()
        if user and user.password == password:
            session["user_id"] = user.id
            return redirect(f"/{user.id}/banner")
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session['user_id'] = 2
        return redirect(f'/banner')
    return render_template('signup.html')

@app.route('/banner',methods=["GET"])
def banner():
    return render_template('banner.html',data=cities)


@app.route('/communitylobby')
def communitylobby():
    return render_template("communitylobby.html",data=cities["chennai"])


@app.route("/group_chat")
def group_chat():
    return render_template("group_chat.html")

if __name__ == "__main__":
    app.run(debug=True)