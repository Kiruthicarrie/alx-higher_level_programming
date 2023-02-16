#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py <mysql username> /
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

# https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy
    # state = session.query(State).filter_by(id=2).first()
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    # print(state.name)
    session.commit()
