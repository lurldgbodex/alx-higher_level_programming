#!/usr/bin/python3
"""
lists all states from the hbtn_0e_0_usa database
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
    user=sys.argv[1], passwd=sys.argv[2], database_name=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    print([row for row in rows])
