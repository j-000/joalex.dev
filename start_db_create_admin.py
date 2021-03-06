import sys
from server import engine
from models import (
    User,
    Base,
    Pawn,
)


def main(pwd):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    User(name='Joao', surname='Oliveira', email='hello@joalex.dev', password=pwd, is_admin=True)


if __name__ == '__main__':
    main(pwd=sys.argv[1])
