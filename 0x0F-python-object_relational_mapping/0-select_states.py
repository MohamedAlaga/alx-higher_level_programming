#!/usr/bin/python3
"""
script that lists all states from the database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 user=argv[1], password=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    data = cursor.fetchall()
    for state in data:
        print(state)
