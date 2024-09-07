#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST  request to the
passed  URL with the email as a parameter, and finally displays the body
of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email as a parameter
    data = {'email': email}

    # Send a POST request with the email as data
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
