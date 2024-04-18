#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username> \
    <mysql password> <database name>
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create a connection to the Database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # An Engine, which the Session will use for connection resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    # Generate database schema
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query to get all City objects with their corresponding State objects
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print all City objects with their corresponding State names
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
