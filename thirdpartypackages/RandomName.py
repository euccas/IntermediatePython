# Random Name
# Fetch and print a random name by performing an HTTP request on http://www.pseudorandom.name/
#
# Hint
# 
# If you set the “User-Agent” header to “curl” you will receive a raw text request from that website instead of an HTML page

import requests

url = "http://www.pseudorandom.name"
myheaders = {
    'User-agent': 'curl'
}
response = requests.get(url, headers=myheaders)

print(response.text)

# Reference
# http://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python

