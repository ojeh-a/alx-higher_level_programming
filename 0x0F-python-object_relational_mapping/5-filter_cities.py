#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all \
    cities of that state using the database hbtn_0e_4_usa

Usage:
    ./4-cities_by_state.py <user> <password> <db> <state name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = """SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))
    cursor.close()
    db.close()
