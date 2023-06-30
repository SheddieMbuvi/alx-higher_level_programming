#!/bin/bash
# Takes in URL & display the body
curl -s -L -X POST "$1" -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD"
