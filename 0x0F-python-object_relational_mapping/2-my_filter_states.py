#!/usr/bin/python3
"""
Takes in an argument and displays all values in
    the table that matches the argument.
usage:
    ./2-my_filter_states.py <user> <password> <db> <search_name>
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}'".
                format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
