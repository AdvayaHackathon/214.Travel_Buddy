from flask import Flask
import auth
from models.model import *
app = Flask(__name__)
app.config['SECRET_KEY']='East'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///TravelBuddy.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(auth.bp)

if __name__ == "__main__":
    app.run(debug=True)