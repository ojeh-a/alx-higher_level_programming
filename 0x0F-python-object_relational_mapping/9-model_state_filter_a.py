#!/usr/bin/python3
"""
Lists all State objects that contain the 
letter `a` from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    # Create conection to engine of db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create metadata
    Base.metadata.create_all(engine)

    # Create instance for engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    query = session.query(State).filter(State.name.like('%a%')).all()

    # Print
    for state in query:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
