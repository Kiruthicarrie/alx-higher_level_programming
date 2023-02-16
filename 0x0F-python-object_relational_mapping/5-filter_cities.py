#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # 1st command-line argument would return the filename that was run
    USER = sys.argv[1]  # 1st command-line argument after executable
    PASSWORD = sys.argv[2]  # 2nd command-line argument after executable
    DB_NAME = sys.argv[3]  # 3rd command-line argument after executable
    USER_INPUT = sys.argv[4]
    HOST = "localhost"
    PORT = 3306

    db = MySQLdb.connect(
        user=USER, passwd=PASSWORD, db=DB_NAME,
        host=HOST, port=PORT, charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM `cities` as `city` \
                INNER JOIN `states` as `state` \
                   ON `city`.`state_id` = `state`.`id` \
                       WHERE `state`.`name` LIKE %s\
                ORDER BY `city`.`id`",
        (USER_INPUT,),
    )
    results = cur.fetchall()
    print(", ".join([city[2] for city in results]))
