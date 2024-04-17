#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all the objects in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to change the name of the state with id 2 to New Mexico
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()

    # Close the session
    session.close()
