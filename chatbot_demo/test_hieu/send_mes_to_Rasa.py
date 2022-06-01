# import requests
# import json

# # API_ENDPOINT = "http://localhost:5005/model/parse"

# # messagePayload = {
# #     'text':'bye'
# # }

# # r = requests.post(url = API_ENDPOINT, data = messagePayload) 


# url = 'http://localhost:5005/webhooks/rest/webhook'
# payload = {'sender': '5330472073648631', 'message': 'Cho hỏi Doanh thu tháng trước'}
# headers = {'content-type': 'application/json'}

# response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}).json()[0]
# print(response)

import requests
import json

access_token = "m-Cd2fr2mWlEuYGEa4333yxhB0cVLif4gV5zExKWt4I0ztWhZLASLwwp2rQUREq9dOPy1fecdNMn_Iuiarp8A8owPas9RuTEWQeL8AbhirYbY3ORyqwXQTU25Zg0A91AlearK9L-hXE_lavGbqVmE9lvOLMNNFKti8vHDv9kjcAyln05XM-B1fA42MkhOx4v-BGcRVnYmWMtkNrgi4Jz4vgVGsAzDTySlTnPPhmE_GImynzqiW7_5ux-RdcEGCyuj-TDEQGDysI4yrqLhJd2JuNcPJkRAj5YoDj58iOuocoInYqLXH2iSBRv8nMn6Bb0XzjM5gOQv6crkMGRHrzcazOtaLx01G"
headers = { "access_token": access_token }
payload = {
  "recipient": {
    "user_id": "8668477534363029464"
  },
  "message": {
    "text": "hello, world!"
  }
}
response = requests.post("https://openapi.zalo.me/v2.0/oa/message", data=json.dumps(payload), headers = headers)
if response.ok:
    print("send success")
else: 
    print("send failed")








