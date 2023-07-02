#!/usr/bin/python3
"""
A python script that takes in a URL, sends a
request to the URL and respond
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
            print('{}'.format(response.info().get('X-Request-id')))
