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
from enum import Enum
from ..config import config
from ..utils import utils

k_host = "http://43.157.39.4:7001"

class Role(str, Enum):
  system    = 'system'
  user      = 'user'
  assistant = 'assistant'

class Model(str, Enum):
  gpt35 = "gpt-3.5-turbo"
  gpt4  = "gpt-4"

class Message: 
  def __init__(self, role: str, content: str):
    self.role = role
    self.content = content

  @property
  def __dict__(self):
    return {
      "role":  self.role,
      "content": self.content,
    }

class ChatRequest:
  def __init__(self, messages: List[Message], model: str):
    self.model = model
    self.messages = messages
    self.temperature = 0.2

  @property
  def __dict__(self):
    return {
      "model":  self.model,
      "messages": list(map(lambda m:m.__dict__, self.messages)),
      "temperature": self.temperature,
    }

class ChatResponse:
  def __init__(self, exception: Exception, message: Message):
    self.exception = exception
    self.message = message

class GPT:
  def chat(self, messages: List[Message], model = Model.gpt35.value) -> ChatResponse:
    request = ChatRequest(messages, model)
    try:
      rsp = self.post("gpt/chat", data=request.__dict__)
      if (rsp["code"] != 0):
        errmsg = rsp["message"] + "(" + str(rsp["code"]) + ")"
        raise ValueError("response is invalid, " + errmsg)
      role = rsp["data"]["role"] if "role" in rsp["data"] else None
      content = rsp["data"]["content"] if "content" in rsp["data"] else None
      return ChatResponse(None, Message(role, content))
    except Exception as ex:
      return ChatResponse(ex, None)

  def post(self, spath: str, data: dict[str, any]) :
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + config.openai_api_key
    } 
    url = os.path.join(k_host, spath)
    rsp = requests.post(url=url, headers=headers, json=data).json()
    code = rsp["statusCode"] if "statusCode" in rsp else -1
    code = rsp["code"] if "code" in rsp else code
    errmsg = rsp["message"] if "message" in rsp else "unknown error"
    errmsg = "\n".join(errmsg) if utils.is_array(errmsg) else errmsg
    data = rsp["data"] if "data" in rsp else None
    return { "code": code, "message": errmsg, "data": data}

gpt = GPT()