from flask import Flask, render_template
from config import ProdConfig, DevConfig
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


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')