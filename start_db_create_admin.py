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
    p1 = Pawn('R')
    p1.add_message('ola')
    p2 = Pawn('S')
    p2.add_message('adeus sdsxx')


if __name__ == '__main__':
    main(pwd=sys.argv[1])
