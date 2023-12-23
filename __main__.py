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

from pypi import (
  logger,
  gpt,
  Role,
  Message,
  GPOIClock,
)

def main():
  logger.info("main")
  result = gpt.chat([Message(Role.user.value, 'Hello!')])
  logger.info("message: %s: %s", result.message.role, result.message.content)
  logger.info("exception: %s", str(result.exception))

  # clock = GPOIClock()
  # clock.start();

  pass

if __name__ == "__main__":
  main()
