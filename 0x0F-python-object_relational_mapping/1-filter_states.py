#!/usr/bin/python3
"""
A script that lists all states with a name starting with 'N' from the
database hbtn_0e_0_usa.

Usage:
./1-filter_states.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL database running on localhost at port 3306
and lists all states, ordered by id in ascending order, that start with 'N'.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select states with names starting with 'N'
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BYid ASC"
            )

    # Fetch and print all rows from the query result
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
