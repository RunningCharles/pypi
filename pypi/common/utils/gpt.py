#
#
#      ┏┛ ┻━━━━━┛ ┻┓
#      ┃　　　　　　 ┃
#      ┃　　　━　　　┃
#      ┃　┳┛　  ┗┳　┃
#      ┃　　　　　　 ┃
#      ┃　　　┻　　　┃
#      ┃　　　　　　 ┃
#      ┗━┓　　　┏━━━┛
#        ┃　　　┃   神兽保佑
#        ┃　　　┃   代码无BUG！
#        ┃　　　┗━━━━━━━━━┓
#        ┃　　　　　　　    ┣┓
#        ┃　　　　         ┏┛
#        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
#          ┃ ┫ ┫   ┃ ┫ ┫
#          ┗━┻━┛   ┗━┻━┛
#
#  Created by CharlesChen on 2023/12/12.


import os
import requests
from typing import List
from ..config import config

k_host = "http://43.157.39.4:7001"

class Message: 
  def __init__(self, role:str, content:str):
    self.role = role
    self.content = content

class MessageResult:
  def __init__(self, error: Exception, message: Message):
    self.error = error 
    self.message = message

class GPT:
  def chat(self):
    data = {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": "Hello!"
        }
      ]
    }
    rsp = self.post('gpt/chat', data=data)
    print('rsp:', str(rsp))
    pass

  def post(self, spath: str, data: dict[str, any]):
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + config.openai_api_key
    } 
    url = os.path.join(k_host, spath)
    print("url: ", url)
    print("headers: ", headers)
    print("data: ", str(data))
    response = requests.post(url, data=data, headers=headers)
    return response

gpt = GPT()