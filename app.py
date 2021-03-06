from flask import (
    Flask, 
    render_template, 
    request, 
    escape,
    flash,
    redirect,
    url_for
)
from config import (
    ProdConfig, 
    DevConfig
)
import os
from dotenv import load_dotenv
from utils import notifyme
from threading import Thread
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


load_dotenv()


app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=[] # defaults are applied to all request types.
)



if os.getenv('ENV') == 'production':
    app.config.from_object(ProdConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    raise NotImplementedError('** ! ENV not set. **')


@app.route('/', methods=['GET', 'POST'])
@limiter.limit('3 per day', methods=['POST'])   # limit only POST of form.
def home():
    if request.method == 'POST':
        email = escape(request.form.get('email'))
        message = escape(request.form.get('message'))

        if not email or not message:
            flash('You need to complete both email and message fields.', 'danger')
            return redirect(url_for('home'))

        flash('Your message has been sent.', 'success')
        Thread(target=notifyme, args=(f'New contact by {email}', message)).start()

        return redirect(url_for('home'))
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(429)
def page_not_found(e):
    return render_template('too_many_emails.html'), 429


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')