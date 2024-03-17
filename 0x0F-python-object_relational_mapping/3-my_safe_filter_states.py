#!/usr/bin/python3
"""
script that lists all states from the database

"""

from sys import argv
import MySQLdb


def clean(query=" "):
    i = 0
    for char in query:
        if char == ";":
            return query[:len(query-i)]
        i += 1
    return query


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 user=argv[1], password=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name like BINARY'{}' \
                   ORDER BY states.id ASC".format(clean(argv[4])))
    data = cursor.fetchall()
    for state in data:
        print(state)
    cursor.close()
    connection.close()
