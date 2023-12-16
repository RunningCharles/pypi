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
#  Created by CharlesChen on 2023/12/16.

from bluezero import adapter
from ..logger import logger

class Bluetooth:
  def __init__(self):
    self.dongle = adapter.Adapter()
    logger.info('address: %s', self.dongle.address)
    logger.info('name: %s', self.dongle.name)
    logger.info('alias: %s', self.dongle.alias)
    logger.info('powered: %s', self.dongle.powered)
    logger.info('pairable: %s', self.dongle.pairable)
    logger.info('pairable timeout: %s', self.dongle.pairabletimeout)
    logger.info('discoverable: %s', self.dongle.discoverable)
    logger.info('discoverable timeout: %s', self.dongle.discoverabletimeout)
    logger.info('discovering: %s', self.dongle.discovering)
    logger.info('discoverable: %s', self.dongle.discoverable)

bluetooth = Bluetooth()