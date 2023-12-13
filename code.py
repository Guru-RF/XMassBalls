# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
import alarm
import time

# config
maxrun = 28800 # max runtine in seconds (8 hours)

pixel_pin = board.GP14
num_pixels = 7

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

pixel_pin_top = board.GP12
num_pixels_top = 6

pixels_top = neopixel.NeoPixel(pixel_pin_top, num_pixels_top, brightness=0.1, auto_write=False)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def color_chase_top(color, wait):
    for i in range(num_pixels_top):
        pixels_top[i] = color
        time.sleep(wait)
        pixels_top.show()
    time.sleep(0.5)


def rainbow_cycle_top(wait):
    for j in range(255):
        for i in range(num_pixels_top):
            rc_index = (i * 256 // num_pixels) + j
            pixels_top[i] = colorwheel(rc_index & 255)
        pixels_top.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

start_time = time.monotonic()
elapsed = time.monotonic()

while elapsed < maxrun:
    elapsed = time.monotonic() - start_time
    print(elapsed)
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)
    
    pixels_top.fill(RED)
    pixels_top.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels_top.fill(GREEN)
    pixels_top.show()
    time.sleep(1)
    pixels_top.fill(BLUE)
    pixels_top.show()
    time.sleep(1)

    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
    
    color_chase_top(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase_top(YELLOW, 0.1)
    color_chase_top(GREEN, 0.1)
    color_chase_top(CYAN, 0.1)
    color_chase_top(BLUE, 0.1)
    color_chase_top(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow


pixels.deinit()
pixels_top.deinit()

# sleep 4 24hrs
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 86400)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
