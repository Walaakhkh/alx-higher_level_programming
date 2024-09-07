#!/usr/bin/python3
"""
This script sends a request to a URL and retrieves
the value of the X-Request-Id variable from the headers.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            headers = response.headers
            x_request_id = headers.get('X-Request-Id')
            if x_request_id is not None:
                print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
