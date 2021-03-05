from flask import Flask
from random import choices
import string

app = Flask(__name__)


config = {
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SESSION_COOKIE_DOMAIN': 'localhost.localdomain',
    'SECRET_KEY': ''.join(choices(string.printable, k=50)),
    'DEBUG': True,
    'ENV': 'development',
    'SERVER_NAME': '127.0.0.1:5000',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///dev.db'
}
app.config.update(**config)


@app.route('/')
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    print(f'Generated SECRET_KEY {config.get("SECRET_KEY")}')
    app.run(port=5000, host='0.0.0.0')