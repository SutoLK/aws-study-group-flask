"""
POSTメソッド呼び出しのためのテストファイル
演習問題用
"""

import requests
import json

url = 'http://ec2-18-176-62-93.ap-northeast-1.compute.amazonaws.com/program'
data = {'title':'banana', 'type':'anime'}
headers = {'content-type':'application/json'}

response = requests.post(url, json.dumps(data), headers=headers)

print(response.text)