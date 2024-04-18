#!/usr/bin/python3
'''
Adds the State Object "Loiusiana" to the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Create Engine.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables stored in this metadata
    Base.metadata.create_all(engine)

    # create a Session class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # add loiusiana state
    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)

    # Close connection
    session.close()
