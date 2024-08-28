#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL="$1"

# Send a request to the URL and display the size of the response body in bytes
curl -sI "$URL" | grep -i 'Content-Length:' | awk '{print $2}' | tr -d '\r'
