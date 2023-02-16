#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
Usage: ./11-model_state_insert.py <mysql username> /
                                  <mysql password> /
                                  <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(USER, PASSWORD, DB_NAME),
        pool_pre_ping=True  # It checks if the connection is
        # still alive and re-connects if not.
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
