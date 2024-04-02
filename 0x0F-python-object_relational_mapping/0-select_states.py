#!/usr/bin/env python3
import sys
import MySQLdb
'''
This script connects to mysql and lists all states from
the database `hbtn_0e_usa`
'''


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

# getting a cursor
    cur = db.cursor()

# query to select states by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

# print
    [print(state) for state in cur.fetchall()]
