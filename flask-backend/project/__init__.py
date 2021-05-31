
from datetime import datetime
import logging
from flask_session import Session
from project.function_used_in_init import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pytz

app = Flask(__name__)


date = datetime.date(datetime.now())
logging.basicConfig(
    filename=f"./log/kusuri_{date.year:04}_{date.month:02}_{date.day:02}.log", level=logging.DEBUG)
app.config['DEBUG'] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = './session_key/'

MAX_CONTENT_LENGTH = 160 * 1024 * 1024  # 16 MB
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

secret = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.secret_key = secret
Session(app)


# ---------------------route-------------------------
@app.route('/')
def index():

    if_database_work_all = database_of_frame_information.query.order_by(
        database_of_frame_information.id).all()
    logging.debug(f"if_database_work_all:{if_database_work_all}")
    for _, if_database_work in enumerate(if_database_work_all):
        logging.debug(f"if_database_work:{if_database_work}")
        show_if_database_work = if_database_work.if_database_work
        
    return f"Hello world,database is {show_if_database_work}!"

app.config.from_object("project.config_database.Config")  # sql的tebal不能大写 # 储存licenses
# from_object (tell the program ,where is the config class )
db = SQLAlchemy(app)

class database_of_frame_information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.now(
        pytz.timezone('Asia/Tokyo')))

    if_database_work = db.Column(db.String(50), nullable=True, unique=True)

    def __init__(self, if_database_work):
        self.if_database_work = if_database_work

    def __repr__(self):
        return "<Task %r>" % self.id
