#!/usr/bin/python3
"""
A script that lists all states where name matches the argument from the
database hbtn_0e_0_usa.

Usage:
./2-my_filter_states.py <mysql_username> <mysql_password> <database_name>
<state_name>

The script connects to a MySQL database running on localhost at port 3306
and lists all matching states, ordered by id in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute SQL query to select states where the name matches the argument
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cur.execute(query)

    # Fetch and print all rows from the query result
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
