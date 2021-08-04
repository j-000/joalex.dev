from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('sqlite:///data.db', convert_unicode=True, connect_args={'check_same_thread': False})
db = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


