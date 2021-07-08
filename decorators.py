from functools import wraps
from flask import (
    request,
    render_template,
    flash
)
from models import User


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        user = User.decode_token(token)
        if user:
            return f(*args, **kwargs)
        else:
            flash('Invalid token - login again.', 'danger')
            return render_template('login.html')
    return wrapper
