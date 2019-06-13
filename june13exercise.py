import requests
import json

# Check out the documentation.
# Make request to get the countries.json file that they talk about in the documentation.
# Examine the structure of the JSON data.
res = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
body = json.loads(res.content)
print(body[0].keys())
print(len(body))

# Pick a country.
print(body[19])

# Extract the URL for the JSON data about the government of the country of your choice 
# (if the country has more than one governmental body - like how Canada has both the House of Commons and the Senate - you can just pick one of them).
gov_url = body[19]['legislatures'][0]['popolo_url']

# Make another request to get that government-specific JSON data.
res2 = requests.get(gov_url)
body2 = json.loads(res2.content)
print(body2.keys())
print(len(body2['persons']))

# Extract the name of one politician from that JSON response and save it in a variable.
name = body2['persons'][3]['name']
print(name)
