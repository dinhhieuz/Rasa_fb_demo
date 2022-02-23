import requests
import json

# API_ENDPOINT = "http://localhost:5005/model/parse"

# messagePayload = {
#     'text':'bye'
# }

# r = requests.post(url = API_ENDPOINT, data = messagePayload) 


url = 'http://localhost:5005/webhooks/rest/webhook'
payload = {'sender': '5330472073648631', 'message': 'Cho hỏi Doanh thu tháng trước'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}).json()[0]
print(response)







