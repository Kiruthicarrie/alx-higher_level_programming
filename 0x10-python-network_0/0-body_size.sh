#!/bin/bash
# bash script that gets the size of the response body
curl -s -I $1 | awk '/^Content-Length/ { print $2 }'
