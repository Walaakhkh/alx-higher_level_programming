#!/bin/bash
# This script sends a GET request to a URL and displays the body if status code is 200
response=$(curl -s -w "%{http_code}" -o response_body.txt "$1")
[ "$response" -eq 200 ] && cat response_body.txt
