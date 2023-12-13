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
#
# ------------------------------------------------------
#         A(11)
#      +---------+
#      |         |
# F(10)|         |B(7)
#      |         |
#      +---G(5)--+
#      |         |
#  E(1)|         |C(4)
#      |         |
#      +---------+    * DP(3)
#          D(2)
#
# ------------------------------------------------------
#
#                          -----
#     +-----+     +-----+         +-----+     +-----+
#     |     |     |     |    *    |     |     |     |
#     +-----+     +-----+         +-----+     +-----+
#     |     |     |     |    *    |     |     |     |
#     +-----+ *   +-----+ *       +-----+ *   +-----+ *
#     ---------   ---------       ---------   ---------
#      DIG(12)     DIG(9)          DIG(8)      DIG(6)
#
# ------------------------------------------------------

from enum import Enum
from ..common import (
  GPIOLevel as Level,
  GPIOLed,
)

HIGH = Level.HIGH
LOW = Level.LOW

class LedPin(Enum):
  a = 26
  b = 19
  c = 13
  d = 6
  e = 5
  f = 11
  g = 9
  dp = 10

class DigPin(Enum):
  one  = 12
  two  = 16
  three = 20
  four  = 21

class DigitValue:
  def __init__(self,
    a: Level, b: Level, c: Level, d: Level,
    e: Level, f: Level, g: Level, dp: Level
  ) -> None:
    self.a  = a
    self.b  = b
    self.c  = c
    self.d  = d
    self.e  = e
    self.f  = f
    self.g  = g
    self.dp = dp

class Digit:
  zero  = DigitValue(HIGH, HIGH,  HIGH, HIGH, HIGH, HIGH, LOW,  LOW)
  one   = DigitValue(LOW,  HIGH,  HIGH, LOW,  LOW,  LOW,  LOW,  LOW)
  two   = DigitValue(HIGH, HIGH,  LOW,  HIGH, HIGH, LOW,  HIGH, LOW)
  three = DigitValue(HIGH, HIGH,  HIGH, HIGH, LOW,  LOW,  HIGH, LOW)
  four  = DigitValue(LOW,  HIGH,  HIGH, LOW,  LOW,  HIGH, HIGH, LOW)
  five  = DigitValue(HIGH, LOW,   HIGH, HIGH, LOW,  HIGH, HIGH, LOW)
  six   = DigitValue(HIGH, LOW,   HIGH, HIGH, HIGH, HIGH, LOW,  LOW)
  seven = DigitValue(HIGH, HIGH,  HIGH, LOW,  LOW,  LOW,  LOW,  LOW)
  eight = DigitValue(HIGH, HIGH,  HIGH, HIGH, HIGH, HIGH, HIGH, LOW)
  nine  = DigitValue(HIGH, HIGH,  HIGH, HIGH, LOW,  HIGH, HIGH, LOW)

class DigitLeds:
  def __init__(self):
    self.a  = GPIOLed(LedPin.a.value)
    self.b  = GPIOLed(LedPin.a.value)
    self.c  = GPIOLed(LedPin.c.value)
    self.d  = GPIOLed(LedPin.d.value)
    self.e  = GPIOLed(LedPin.e.value)
    self.f  = GPIOLed(LedPin.f.value)
    self.g  = GPIOLed(LedPin.g.value)
    self.dp = GPIOLed(LedPin.dp.value)

class ClockDigs:
  def __init__(self):
    self.one    = GPIOLed(DigPin.one.value)
    self.two    = GPIOLed(DigPin.two.value)
    self.three  = GPIOLed(DigPin.three.value)
    self.four   = GPIOLed(DigPin.four.value)
