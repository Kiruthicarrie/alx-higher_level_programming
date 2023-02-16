#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                              <mysql password> \
                              <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # 1st command-line argument would return the filename that was run
    USER = sys.argv[1]  # 1st command-line argument after executable
    PASSWORD = sys.argv[2]  # 2nd command-line argument after executable
    DB_NAME = sys.argv[3]  # 3rd command-line argument after executable
    HOST = "localhost"
    PORT = 3306

    db = MySQLdb.connect(
        user=USER, passwd=PASSWORD, db=DB_NAME,
        host=HOST, port=PORT, charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT `city`.`id`, `city`.`name`, `state`.`name`\
        FROM `cities` as `city` \
            INNER JOIN `states` as `state` \
                ON `city`.`state_id` = `state`.`id` \
                    ORDER BY `city`.`id`"
    )
    [print(city) for city in cur.fetchall()]
