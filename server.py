from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager


app = Flask(__name__)

engine = create_engine('sqlite:///data.db', convert_unicode=True, connect_args={'check_same_thread': False})
db = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


load_dotenv()

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=[] # defaults are applied to all request types.
)

login_manager = LoginManager()
login_manager.init_app(app)
