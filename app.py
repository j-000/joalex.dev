import os
import config
from flask import Flask, send_from_directory


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


@app.route('/cv')
def cv():
    return send_from_directory('static', 'my_cv_dev_joao.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')