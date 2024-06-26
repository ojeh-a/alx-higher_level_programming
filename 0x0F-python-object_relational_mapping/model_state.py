#!/usr/bin/python3
'''
Contains the class definition of a State
and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    '''
    Class definition for State object
    '''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
