#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the body response in the specified format
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
