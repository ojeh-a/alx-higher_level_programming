#!/usr/bin/python3
"""
Deletes all State Objects with a name containing the letter 'a' from
the database `hbtn_0e_6_usa`
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    # Create Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    delete_states = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete_states:
        session.delete(state)

    session.commit()
