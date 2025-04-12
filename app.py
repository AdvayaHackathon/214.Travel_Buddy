from flask import Flask,render_template,redirect,session,request,url_for
from models.model import *
app = Flask(__name__)
app.config['SECRET_KEY']='East'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///TravelBuddy.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
citys=["Chennai","Bengaluru","Hyderabad","Odisha"]
db.init_app(app)
with app.app_context():
    db.create_all()

cities={"Chennai":{1:"Fairlands",2:"Marketplace",3:"3 roads",4:"4 roads",5:"Old bus stand",6:"New bustand"},
        "Bengaluru":{1:"Bengaluru palace",2:"Cubbon park",3:"UB city",4:"Phoneix marketcity",5:"V.V.puram",6:"Muthyalamaduvu"},
        "Hyderabad":{1:"Charminar",2:"Jubilee hills",3:"HITEC city",4:"Shaikpet",5:"Secundarnad",6:"Vijayawada"},
        "Odisha":{1:"Konarak",2:"Bhubhaneswar",3:"Cuttack",4:"gangai",5:"Jajapur",6:"Ganjam"}}
@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST',"GET"])
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
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        email=request.form.get("email")
        phone_number=request.form.get("phone")
        place=request.form.get("place")
        users=User(username=username,password=password,email=email,phone_number=phone_number,city=place)
        db.session.add(users)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/<int:cur_log>/banner',methods=["GET","POST"])
def banner(cur_log):
    return render_template('banner.html',cur_log=cur_log,data=cities)


@app.route('/<int:cur_log>/<int:city>/communitylobby')
def communitylobby(cur_log,city):
    return render_template("communitylobby.html",cur_log=cur_log,city=city,data=cities[citys[city-1]],cit=citys[city-1])


@app.route("/<int:cur_log>/<int:city>/<int:group>/group_chat")
def group_chat(cur_log,city,group):
    return render_template("group_chat.html",cur_log=cur_log,city=city,group=group,name=cities[citys[city-1]][group])

if __name__ == "__main__":
    app.run(debug=True)