#!/usr/bin/python3
"""
prints all rows from a db
"""


if __name__ == '__main__':
    import sys
    import MySQLdb


    dbConnect = MySQLdb.connect(host='localhost', port=3306,
                        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = dbConnect.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    dbConnect.close()
