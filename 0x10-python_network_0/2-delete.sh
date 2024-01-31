#!/bin/bash
# Sends DELETE request to URL passed as the first argument and displays the body of the response.
curl -sX DELETE "$1"
