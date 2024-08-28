#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sL -X GET 0.0.0.0:5000/catch_me -H "User-Agent: HolbertonSchool" -b "user_id=98"