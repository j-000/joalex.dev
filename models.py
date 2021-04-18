from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from server import db
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    Boolean,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship
import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
import humanize


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


class Pawn(Base):
    __tablename__ = 'pawns'

    query = db.query_property()
    id = Column(Integer, primary_key=True)
    messages = relationship("Message", backref="pawn")
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    name = Column(String(20), nullable=False)

    def __init__(self, name):
        self.name = name
        db.add(self)
        db.commit()

    def __repr__(self):
        return f'<Pawn {self.name} >'

    def get_total_messages(self):
        return len(self.messages)

    def get_last_message_timestamp(self):
        if len(self.messages) > 0:
            msg_t = self.messages[-1].timestamp
            delta = datetime.datetime.utcnow() - msg_t
            return humanize.naturaltime(delta)
        return 'No messages'

    def add_message(self, message):
        Message(message, self.id)


class Message(Base):
    __tablename__ = 'messages'

    query = db.query_property()
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow)
    text = Column(Text())
    pawn_id = Column(Integer, ForeignKey('pawns.id'), nullable=True)

    def __init__(self, text, p_id):
        self.pawn_id = p_id
        self.text = text
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()

