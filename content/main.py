import os
import time
import esp32
import sgp30
from machine import UART,Pin, I2C, SoftSPI
from bme680 import *
from sdcard import SDCard


def collect_sensors_data(interval):
    """
    interval -> seconds
    Function takes data from bme680 ,sgp30 and also reads internal esp32 temperature
    than store data on sd card
    
    """

    # Define pinouts for sd card reader and sensors connected parallel using i2c protocol
    # Pinout may change if you got different version of esp32 board
    # Alternate pinout:
    #     spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
    #     sd = SDCard(spisd, Pin(27))

    spisd = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
    sd = SDCard(spisd, Pin(5))
    i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
    # Possible to define scl, sda pins as pull_up
    # i2c = I2C(1, scl=Pin(22, Pin.PULL_UP), sda=Pin(21, Pin.PULL_UP), freq=10000)

    # Call instance of libraries class
    sgp = sgp30.Adafruit_SGP30(i2c)
    bme = BME680_I2C(i2c)

    # Mount sd card and change directory
    vfs = os.VfsFat(sd)
    os.mount(vfs, '/sd')
    os.chdir('sd')

    # Infinitie loop in witch data from sensors are append to csv file
    while True:
        f = open("data.csv", 'a')
        co2eq, tvoc = sgp.iaq_measure()
        raw_temp = esp32.raw_temperature()
        tc = (raw_temp-32.0)/1.8
        f.write(f"{tc};{round(bme.temperature,1)};{round(bme.humidity,1)};{int(bme.pressure)};{bme.gas};{co2eq};"
                f"{tvoc}"+"\n")
        f.close()
        print("data collected and saved")
        time.sleep(interval)


# Call function
collect_sensors_data(1)