#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept curl -s -I $1 | awk '/^Allow/ {for( i=2; i<=NF;i++) printf " "$i; print""}'
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
