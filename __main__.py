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

from bluezero import adapter

from pypi import (
  logger,
  gpt,
  GPOIClock,
  bluetooth,
)

def main():
  logger.info("main")
  result = gpt.chat()
  logger.info("result: %s", str(result))

  # clock = GPOIClock()
  # clock.start();

  pass

if __name__ == "__main__":
  main()
