#  Happy Birthday Will!

#################################################################################################
#                              It's So Over.....We're So Back  Meter
#################################################################################################
#                                                                                               #
#                                    .................                                          #
#                             ..............................                                    #
#                         .........                      .......                                #
#                      .......                               .......                            #
#                    .....                                      ......                          #
#                  .....                                           .....                        #
#                .....       ...                                     .....                      #
#               ....         .....                                    .....                     #
#              ....            ......                                  .....                    #
#             ....                .....                                  ....                   #
#             ....                  ......                               ....                   #
#            ....                      ...........                        ....                  #
#            ....                       ...........                       ....                  #
#            ....                       ...........                       ....                  #
#            ....                        .........                       .....                  #
#             ....                                                       ....                   #
#             .....                                                     ....                    #
#              .....                                                   .....                    #
#               .....                                                 ....                      #
#                 .....                                             .....                       #
#                   .....                                         .....                         #
#                     ....                                      .....                           #
#                                                                                               #
#################################################################################################                                                                             


# for Adafruit KN2040 board.  https://learn.adafruit.com/adafruit-kb2040/                                                 
                                                                         
import time
import board
import neopixel
import busio
import board
import pwmio
import random

#Included in onboard lib is the following
#asyncio, _bleio, _pixelmap, adafruit_bus_device, adafruit_pixelbuf, aesio, alarm,
#  analogbufio, analogio, array, atexit, audiobusio, audiocore, audiomixer, audiomp3,
#  audiopwmio, binascii, bitbangio, bitmaptools, bitops, board, builtins, builtins.pow3,
#  busio, busio.SPI, busio.UART, collections, countio, digitalio, displayio, errno, floppyio,
#  fontio, framebufferio, getpass, gifio, i2ctarget, imagecapture, io, json, keypad, keypad.KeyMatrix, 
# keypad.Keys, keypad.ShiftRegisterKeys, math, microcontroller, msgpack, neopixel_write, nvm, onewireio,
#  os, os.getenv, paralleldisplay, pulseio, pwmio, qrio, rainbowio, random, re, rgbmatrix, rotaryio, rp2pio,
#  rtc, sdcardio, select, sharpdisplay, storage, struct, supervisor, synthio, sys, terminalio, time, touchio, 
# traceback, ulab, usb_cdc, usb_hid, usb_midi, vectorio, watchdog, zlib




uart = busio.UART(board.TX, board.RX, baudrate=115200)  # Initialize UART communication
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)  # Initialize NeoPixel
led = pwmio.PWMOut(board.D4, frequency=5000, duty_cycle=0)  # Initialize LED
time.sleep(5)  # Wait for 5 seconds

# Warm up the gauge 
for i in range(4):
    print("Booting...")  # Print booting message
    pixel.fill((128, 0, 128))  # Set pixel color to purple
    led.duty_cycle = 1  # Turn on LED
    pixel.brightness = 1  # Set pixel brightness to maximum
    time.sleep(0.3)  # Wait for 2 seconds
    led.duty_cycle = 0  # Turn off LED
    pixel.brightness = 0  # Set pixel brightness to minimum
    time.sleep(0.3)  # Wait for 2 seconds


while True:  # Main loop
    start_time = time.monotonic()  # Get the current time
    print("Starting main loop")  # Print starting message


    # It's over state
    uart.write(b"It's so over \n")  # Send message over UART
    print("It's so over")  # Print message
    while time.monotonic() - start_time < 5:  # Loop for 5 seconds
        brightness = float(0)  # Set brightness to 0
        noise = float(0.1* random.random())  # Add random noise
        led.duty_cycle = int( ( brightness + noise)*255)  # Set LED brightness
        pixel.brightness = brightness + noise  # Set pixel brightness
        pixel.fill((255, 0, 0))  # Set pixel color to red
        #print(f"Brightness: {brightness}")  # Print brightness
        #print(f"Noise: {noise}")  # Print noise
        time.sleep(0.01)  # Wait for 10 milliseconds



     # It's over state
    uart.write(b"We're so back \n")  # Send message over UART
    print("We're so back")  # Print message
    while time.monotonic() - start_time < 15:  # Loop for 15 seconds
        brightness = float(0.5)  # Set brightness to 0.5
        noise = float(0.2 * random.random())  # Add random noise
        led.duty_cycle = int( ( brightness + noise)*255)  # Set LED brightness
        pixel.brightness = brightness + noise  # Set pixel brightness
        pixel.fill((0, 255, 0))  # Set pixel color to green
        #print(f"Brightness: {brightness}")  # Print brightness
        #print(f"Noise: {noise}")  # Print noise
        time.sleep(0.01)  # Wait for 10 milliseconds

