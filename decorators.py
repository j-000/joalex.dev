from functools import wraps
from flask import (
    request,
    redirect,
    url_for
)
import jwt
from server import app


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if token:

            print(token)

            email = jwt.decode(token, key=app.config.get('SECRET_KEY'), algorithms='HS256')
            print(email)
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
