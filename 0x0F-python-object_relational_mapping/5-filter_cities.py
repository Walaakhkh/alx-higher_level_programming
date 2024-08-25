#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database hbtn_0e_4_usa

Usage:
./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
<state_name>

The script connects to a MySQL database running on localhost at port 3306
and lists all cities of the specified state, sorted by cities.
id in ascending order.
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

    # Execute SQL query to join cities and states tables and retrieve results
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Print the city names, separated by a comma
    print(", ".join(row[0] for row in rows))

    # Close the cursor and the database connection
    cur.close()
    db.close()
