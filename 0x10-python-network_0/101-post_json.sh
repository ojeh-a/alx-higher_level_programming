#!/bin/bash
# Sends a JSON POST request to URL passed as first argument and displays body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
