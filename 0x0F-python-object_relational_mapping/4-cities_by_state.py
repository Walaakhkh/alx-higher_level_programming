#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa.

Usage:
./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL database running on localhost at port 3306
and lists all cities with their state names, ordered by
cities.id in ascending order.
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

    # Execute SQL query to join cities and states tables and retrieve results
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and print all rows from the query result
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
