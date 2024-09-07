#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the letter (or default to an empty string if no argument is provided)
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the payload with the letter as the value of 'q'
    payload = {'q': letter}

    # Send a POST request to the server
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        # Attempt to parse the JSON response
        json_response = response.json()

        # Check if the JSON response is not empty
        if json_response:
            # Display the id and name
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            # Display 'No result' if the JSON response is empty
            print("No result")
    except ValueError:
        # Display 'Not a valid JSON' if the response is not a valid JSON
        print("Not a valid JSON")
