#!/bin/bash
# sends a request to URL, and displays the size of the body of the response
curl -is $1| grep -oP 'Content-Length: \K\d+'
