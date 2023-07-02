#!/usr/bin/python3
"""
Takes in a URL and an Email, sends a
POST requst to the parsed URL
"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    print('{}'.format(response.text))
