#!/bin/bash
# takes a url, sends a rewquest to the url, and d displays the size of the response body

curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
