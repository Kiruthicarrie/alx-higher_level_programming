#!/usr/bin/python3
"""
Lists all states that matches user's input.
Usage:
------
./2-my_filter_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # 1st command-line argument would return the filename that was run
    USER = sys.argv[1]  # 1st command-line argument after executable
    PASSWORD = sys.argv[2]  # 2nd command-line argument after executable
    DB_NAME = sys.argv[3]  # 3rd command-line argument after executable
    USER_INPUT = sys.argv[4]
    HOST = "localhost"
    PORT = 3306

    db = MySQLdb.connect(
        user=USER, passwd=PASSWORD,
        db=DB_NAME, host=HOST, port=PORT
        )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM `states` \
            WHERE `name` LIKE BINARY'{:s}' \
        ORDER BY id".format(
            USER_INPUT
        )
    )

    result = cur.fetchall()
    [print(state) for state in result]

    cur.close()
    db.close()
