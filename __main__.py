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
  GPOIClock,
)

def main():
  # result = gpt.chat([{"role": "user", "content": "Hello!"}])
  # logger.info('error: %s',str(result.error))
  # logger.info('message: %s', result.message)
  clock = GPOIClock()
  clock.start();

if __name__ == '__main__':
  main()
