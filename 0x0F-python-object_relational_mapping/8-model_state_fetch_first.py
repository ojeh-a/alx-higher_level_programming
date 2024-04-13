#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    # Create a new Engine instance.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database; print the first State object.
    first_state = session.query(State).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session.
    session.close()