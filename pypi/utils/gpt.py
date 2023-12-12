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

from typing import List
from ..config import config
from openai import OpenAI

class Message: 
  def __init__(self, role:str, content:str):
    self.role = role
    self.content = content


class MessageResult:
  def __init__(self, error: Exception, message: Message):
    self.error = error 
    self.message = message

class GPT:
  def __init__(self):
    self.client = OpenAI(
      api_key=config.openai_api_key,
      organization=config.openai_org,
    )
  
  def chat(self, messages: List[Message], model = 'gpt-3.5-turbo') -> MessageResult:
    try:
      completion = self.client.chat.completions.create(
        model=model,
        messages=messages,
      )
      return MessageResult(None, completion.choices[0].message)
    except Exception as error:
      return MessageResult(error, None)

gpt = GPT()