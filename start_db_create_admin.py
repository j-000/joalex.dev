import sys
from server import engine
from models import (
    User,
    Base
)


def main(pwd):
    User(name='Joao', surname='Oliveira', email='hello@joalex.dev', password=pwd, is_admin=True)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main(pwd=sys.argv[1])