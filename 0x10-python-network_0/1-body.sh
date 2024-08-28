#!/bin/bash
# This script sends a GET request to a URL and displays the body if status code is 200, handling redirects
curl -s -L -w "%{http_code}" -o /tmp/response_body.txt "$1" | grep -q '200' && cat /tmp/response_body.txt
