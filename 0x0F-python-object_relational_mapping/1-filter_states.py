#!/usr/bin/python3
"""
Lists all states with a name starting with `N` from database `hbtn_0e_0_usa`
usage:
    ./1-filter_states.py <user> <pass> <db>
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    states = c.fetchall()
    [print(state) for state in states if state[1][0] == "N"]
