import os
from flask import (
    render_template,
    request, 
    escape,
    flash,
    redirect,
    url_for,
    jsonify,
    make_response,
    send_from_directory
)
from flask_login import (
    logout_user,
    login_user
)
from decorators import (
    jwt_required
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
from models import (
    User,
    Pawn,
)
import jwt
from werkzeug.utils import secure_filename
from natsort import natsorted

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
        return redirect(url_for('home'))
    return render_template('home.html')


@app.route('/cv')
def cv():
    return send_from_directory('static', 'my_cv_dev_joao.pdf', as_attachment=True)

########################################################################################
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(success=False, message='No file part')
        file = request.files['file']
        if file.filename == '':
            return jsonify(success=False, message='No file part')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config.get('UPLOAD_FOLDER'), filename))
            return jsonify(success=True)
    return jsonify(method='POST only')


@app.route('/images')
@jwt_required
def screenshots():
    pawn_files = natsorted(os.listdir(app.config.get('UPLOAD_FOLDER')))
    return render_template('protected/screenshots.html', pawn_files=pawn_files)


@app.route('/kl', methods=['GET', 'POST'])
def kl():
    if request.method == 'POST':
        data = request.json.get('d')
        pawn = request.json.get('p', 'f')
        p_obj = Pawn.query.filter_by(name=pawn).first()
        if p_obj:
            p_obj.add_message(data)
        else:
            p = Pawn(name=pawn)
            p.add_message(data)
        return jsonify(success=True)
    return jsonify(secret=1)


@app.route('/admin/messages/<pawn_id>')
@jwt_required
def messages(pawn_id):
    pawn = Pawn.query.get(pawn_id)
    msgs = []
    if pawn:
        msgs = sorted(
            pawn.messages,
            key=lambda x: x.timestamp,
            reverse=True
        )
    return render_template('protected/messages.html', messages=msgs, pawn=pawn)


@app.route('/admin', methods=['GET', 'POST'])
@jwt_required
def admin():
    pawns = Pawn.query.all()
    return render_template('protected/admin.html', pawns=pawns)

##############################################


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            if user_exists.valid_password(password):
                login_user(user_exists)
                session_token = jwt.encode({'user': email}, key=app.config.get('SECRET_KEY'), algorithm='HS256')
                resp = make_response(redirect(url_for('admin')))
                resp.set_cookie('token', session_token)
                return resp
            flash('Invalid password.', 'danger')
            return render_template('login.html')
        flash('Invalid email.', 'danger')
        return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
@jwt_required
def logout():
    logout_user()
    flash('Bye for now.', 'success')
    return render_template('home.html')


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