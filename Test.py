# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the TSL2591 sensor.  Will print the detected light value
# every second.
import time
import board
import adafruit_tsl2591

OUTPUT_FILE = "out.csv"

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# You can optionally change the gain and integration time:
# sensor.gain = adafruit_tsl2591.GAIN_LOW (1x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MED (25x gain, the default)
# sensor.gain = adafruit_tsl2591.GAIN_HIGH (428x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MAX (9876x gain)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS (100ms, default)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS (200ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS (300ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS (400ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS (500ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS (600ms)

# Read the total lux, IR, and visible light levels and print it every second.
with open(OUTPUT_FILE, "w") as out:
    out.write("time,Gesamthelligkeit,Infrarotlicht,Sichtbares Licht,Gesampspektrun\n")

while True: 
    try:
        sl, si, sv, sf = sensor.lux, sensor.infrared, sensor.visible, sensor.full_spectrum

    except:
        print(f"Messfehler!")
        continue

    out_string = f"{time.strftime('%x %X')},{sl},{si},{sv},{sf}\n"

    if max([sl, si, sv, sf]) > 100_000 or min([sl, si, sv, sf]) < 0:
        print("Ungültiger sensor wert: ", out_string)
        time.sleep(.5)
        continue

    print(out_string)

    try:
        with open(OUTPUT_FILE, "a") as out:
            out.write(out_string)

    except:
        print("Fehler beim schreiben der Datei!")

    time.sleep(1)
