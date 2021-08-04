import os
import config
from server import app
from flask import (
    render_template,
    send_from_directory
)



if os.getenv('ENV') == 'production':
    app.config.from_object(config.ProdConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(config.DevConfig)
else:
    raise NotImplementedError('** ! ENV not set. **')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/cv')
def cv():
    return send_from_directory('static', 'my_cv_dev_joao.pdf', as_attachment=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')