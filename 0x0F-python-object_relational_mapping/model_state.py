#!/usr/bin/python3
"""
This module defines the State class and creates the table in the MySQL database
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# Define the Base
Base = declarative_base()

class State(Base):
    """
    State class maps to the 'states' table in the database.
    """
    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Main code to create the database and table
if __name__ == "__main__":
    # Create the engine using the provided MySQL credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create all tables in the engine
    Base.metadata.create_all(engine)
