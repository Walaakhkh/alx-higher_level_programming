#!/bin/bash
# This script sends a GET request to a URL and displays the body if status code is 200
curl -s -L "$1" | awk 'NR==1{if($0 ~ /200/){print $0}}'
