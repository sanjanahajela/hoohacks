# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = 'your customerId here'
apiKey = '5dd0750fab026e87a6d13f99f4b0f062'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')