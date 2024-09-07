#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    # Get the username and personal access token from command-line arguments
    Walaakhkh = sys.argv[1]
    personal_access_token = sys.argv[2]

    # GitHub API URL for user information
    url = 'https://api.github.com/user'

    # Perform Basic Authentication using the username and personal access token
    response = requests.get(
            url, auth=(Walaakhkh, personal_access_token)
            )

    # Check the response status code
    if response.status_code == 200:
        # Print the user ID from the JSON response
        user_data = response.json()
        print(user_data.get('id'))
    else:
        # Print None if the authentication failed or the user was not found
        print(None)
