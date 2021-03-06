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


load_dotenv()


app = Flask(__name__)


if os.getenv('ENV') == 'production':
    app.config.from_object(ProdConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    raise NotImplementedError('** ! ENV not set. **')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = escape(request.form.get('email'))
        message = escape(request.form.get('message'))

        if not email or not message:
            flash('You need to complete both email and message fields.', 'danger')
            return redirect(url_for('home'))

        flash('Your message has been sent.', 'success')
        
        # handle message 

        return redirect(url_for('home'))
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')