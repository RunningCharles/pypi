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
#  Created by CharlesChen on 2023/12/13.

from ..common import (
  GPIOLevel as Level,
  GPIOLed,
  reset_leds,
)
from .defines import (
  Digit,
  DigitLeds,
  ClockDigs,
  DigitValue,
)

class GPOIClock:
  def __init__(self):
    self.leds = DigitLeds()
    self.digs = ClockDigs()
    self.dig_pins = self.digs.__dict__.values()

  def display_digit(self, dig: GPIOLed, digit: DigitValue):
    reset_leds(self.dig_pins, Level.HIGH)