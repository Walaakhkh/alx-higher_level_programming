#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>")
        return

    # Extract arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the database connection engine
    engine = create_engine(f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query the State table
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    main()
