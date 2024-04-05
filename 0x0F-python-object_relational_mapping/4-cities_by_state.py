#!/usr/bin/python3
"""
Lists all `cities` from the database `hbtn_0e_4_usa`

Usage:
    ./4-cities_by_state.py <user> <passwd> <db>
"""
import sys
import MySQLdb as d

if __name__ == "__main__":
    db = d.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             ORDER BY cities.id ASC
    """
    cur.execute(query)
    rows = cur.fetchall()
    [print(row) for row in rows]

    cur.close()
    db.close()
