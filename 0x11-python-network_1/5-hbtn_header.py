#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the provided URL
    response = requests.get(url)

    # Get the value of the 'X-Request-Id' from the response headers
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value of the 'X-Request-Id'
    print(x_request_id)
