#!/bin/bash
# Bash script that displays the size of the body
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
