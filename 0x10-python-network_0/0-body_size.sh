#!/bin/bash
# Takes in a URL, sends a request tp that URL, and displays the size of the body response
curl -s "$1" | wc -c
