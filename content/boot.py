# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import os
import time
import esp32
import sgp30
from machine import UART,Pin, I2C, SoftSPI
from bme680 import *
from sdcard import SDCard