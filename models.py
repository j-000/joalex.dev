from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from server import db
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    Boolean,
    Text
)
import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'

    query = db.query_property()
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    name = Column(String(20), nullable=False)
    surname = Column(String(20))
    email = Column(String(50), nullable=False)
    password = Column(String(300), nullable=False)
    is_admin = Column(Boolean(), default=False)

    def __repr__(self):
        return f'< User {self.id}: {self.name} {self.surname} >'

    def __init__(self, name, email, password, surname=None, is_admin=False):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        if surname:
            self.surname = surname
        if is_admin:
            self.is_admin = True
        db.add(self)
        db.commit()

    def valid_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Message(Base):
    __tablename__ = 'messages'

    query = db.query_property()
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    email = Column(String(30))
    text = Column(Text())

    def __init__(self, email, text):
        self.email = email
        self.text = text
        db.add(self)
        db.commit()
