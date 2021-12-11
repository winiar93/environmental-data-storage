# environmental-data-storage
esp32 logger supported by micropython with sgp30, bme680, and sd card reader

## What is it? what is that for? 

Esp32 micropython based project was created for collecting data like temperature, humidity, pressure, gas resistance from bme680, TVOC and eCO2.

You can read more about sgp30 [here](https://github.com/winiar93/MicroLogger).

That side project will help to further develop the main [project](https://github.com/winiar93/raspberry-pi-bme680-logger).

There is visible correlation between bme680 sensor resistance readings and values from sgp30 which are VOCs and eCO2.
Higher concentration of VOCs causes lower sensor resistance.
Lower concentration of VOCs causes higher sensor resistance.
Also for better data quality it will be necessary to change place of measurements few times after some days.

So the goal will be creating neural network model to estimate possible VOCs with whole collected data.
Using that model it could be possible to build e.g. data pipeline for
calculations and after that store data on cloud or in relational database. 

#### Libraries in this project:
* [Adafruit_CircuitPython_BME680](https://github.com/adafruit/Adafruit_CircuitPython_BME680)
* [Adafruit_CircuitPython_SGP30](https://github.com/adafruit/Adafruit_CircuitPython_SGP30)
* [SD card ](https://techtotinker.blogspot.com/2021/04/023-esp32-micropython-how-to-use-sd.html)

[Download micropython](https://micropython.org/download/ESP32_S2_WROVER/)

#### Wiring diagram
![image info](wiring_diagram.jpg)
