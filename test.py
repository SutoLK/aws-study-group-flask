"""
POSTメソッド呼び出しのためのテストファイル
"""

import requests
import json

url = 'http://ec2-18-176-62-93.ap-northeast-1.compute.amazonaws.com/item'
data = {'name':'sofa', 'price':90000}
headers = {'content-type':'application/json'}   #application/jsonはjson形式でデータを送るよ、という宣言

response = requests.post(url, json.dumps(data), headers=headers)

print(response.text)