#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the status code is >= 400 and print the error code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
