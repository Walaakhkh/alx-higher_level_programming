#!/usr/bin/python3
"""
This script fetches a URL using the urllib package and displays
the body of the response in a specific format.
"""

import urllib.request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
