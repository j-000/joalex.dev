import os
from threading import Thread
from flask import (
    render_template,
    request, 
    escape,
    flash,
    redirect,
    url_for,
    jsonify
)
from flask_login import (
    login_required,
    login_user,
    logout_user,
)
from server import (
    login_manager,
    limiter,
    app
)
from config import (
    ProdConfig, 
    DevConfig
)
from utils import notifyme
from models import (
    User,
    Message
)


if os.getenv('ENV') == 'production':
    app.config.from_object(ProdConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    raise NotImplementedError('** ! ENV not set. **')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    flash('Please log in.', 'info')
    return redirect(url_for('home'))


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
        Message(email=email, text=message)
        Thread(target=notifyme, args=(f'New contact by {email}', message)).start()

        return redirect(url_for('home'))
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/kl', methods=['GET', 'POST'])
@limiter.limit('100 per day', methods=['POST'])
def kl():
    if request.method == 'POST':
        data = request.json.get('d')
        message = escape(data)
        Message(email='***KL***', text=message)
        return jsonify(success=True)
    return jsonify(method='POST', params='d')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            if user_exists.valid_password(password):
                login_user(user_exists)
                return redirect(url_for('admin'))
            flash('Invalid password.', 'danger')
            return redirect(url_for('login'))
        flash('Invalid email.', 'danger')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/admin')
@login_required
def admin():
    messages = sorted(
        Message.query.all(),
        key=lambda x: x.timestamp,
        reverse=True
    )
    return render_template('protected/admin.html', messages=messages)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bye for now.', 'success')
    return redirect(url_for('home'))


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