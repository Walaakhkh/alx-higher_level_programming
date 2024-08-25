#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@localhost:3306/{database}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object
    try:
        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
