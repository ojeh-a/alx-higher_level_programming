#!/usr/bin/python3
"""
Takes arguments and displays all values in the table
that matches the argument, safe from MySQL injections

Usage:
    ./3_safe_filter_states.py <user> <pass> <db> <argument>
"""
import sys
import MySQLdb


if __name__ == '__main__':
    # Connect to server
    conn = MySQLdb.connect(user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    # Define the query with a placeholder
    query = "SELECT * FROM `states`"

    # Execute the query with user input as parameters
    cur.execute(query)

    # Fetch and print results
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]

    # Close cursor and connection
    cur.close()
    conn.close()
