import os
import config
from flask import Flask, send_from_directory, render_template, request
import json

def create_app():
    app = Flask(__name__)

    if os.getenv('ENV') == 'production':
        app.config.from_object(config.ProdConfig)
    elif os.getenv('ENV') == 'development':
        app.config.from_object(config.DevConfig)
    else:
        raise NotImplementedError('** ! ENV not set. **')
    return app


app = create_app()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cv')
def cv():
    return send_from_directory('static', 'my_cv_dev_joao.pdf', as_attachment=True)


@app.route('/log-geo')
def loggeo():
    geo = request.args.get('geo')
    with open('file.json', 'a+') as f:
        f.write(json.dumps({request.headers.get('X-Real-Ip', request.environ.get('HTTP_X_REAL_IP')): str(geo)}, indent=5))
    return ''

@app.route('/share-folder')
def share_folder():
    j = {}
    for a in list(filter(lambda x: x > 'a', dir(request))):
        j.update({a.ljust(20): str(getattr(request, a))})
    with open('file.json', 'a+') as f:
        f.write(json.dumps(j, indent=5))
        f.write('\n\n')
    return render_template('sf.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')