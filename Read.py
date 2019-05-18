#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#
import time, os, subprocess
import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(12,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)
#GPIO.setup(24,GPIO.OUT)
#GPIO.setup(26,GPIO.OUT)
#Button
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(06, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(04, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setwarnings(False)
check_RFID = True
read_tour = False

# Capture SIGINT for cleanup when the script is aborted
def uid_2_num(uid):
        n = 0
        for i in range(0,5):
                n = n * 256 + uid[i]
        return n

def end_read(signal,frame):
    global check_RFID
    global tour_de_garde
    print "Ctrl+C captured, ending read."
    check_RFID = False
    exit()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Valid Tokens
#token = open("uid","r")
#token = token.read()
#print(token)
validTokens = ["236630443117","301642601442","110268710962"]
#for x in validTokens:
#       print(x)
# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while check_RFID:
        time.sleep(0.025)
# while continue_reading:
# Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
# Get the UID of the card
# Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

# If a card is found
        if status == MIFAREReader.MI_OK:
                print "Card detected"
                if str(uid_2_num(uid)) in validTokens:
                        check_RFID = False
                        tour_de_garde = True
                        verification_du_tour = True
                        Jeton_utiliser = str(uid_2_num(uid))
                        temps = datetime.datetime.now()
                        tour_de_garde = '{\n"Jeton" : "'+str(uid_2_num(uid))+'", \n"Start" : "'+temps.strftime("%Y-%m-%d %H:%M:%S")+'", \n'
                        GPIO.cleanup()
                        print "found"
if tour_de_garde:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(26,GPIO.OUT)
#Button
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(06, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(04, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Turn on LED

        GPIO.output(18,GPIO.HIGH)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(26,GPIO.HIGH)
#Turn LED off
        time.sleep(1)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(26,GPIO.LOW)

        sequence = ""
        while read_tour:
                sleep(0.025)
                if GPIO.input(06) == GPIO.HIGH:
                        print("Pin 23 Button 2 was pushed")
                        GPIO.output(26,GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(26,GPIO.OUT)
                        print("2")
                else:
                        GPIO.output(26,GPIO.OUT)
                if GPIO.input(22) == GPIO.HIGH:
                        print("Pin 23 Button 2 was pushed")
                        GPIO.output(12,GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(12,GPIO.OUT)
                        print("2")
                else:
                        GPIO.output(12,GPIO.OUT)
                if GPIO.input(27) == GPIO.HIGH:
                        print("Pin 23 Button 2 was pushed")
                        GPIO.output(24,GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(24,GPIO.OUT)
                        print("2")
                else:
                        GPIO.output(24,GPIO.OUT)
                if GPIO.input(26) == GPIO.HIGH:
                        print("Pin 23 Button 2 was pushed")
                        GPIO.output(23,GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(23,GPIO.OUT)
                        print("2")
                else:
                        GPIO.output(23,GPIO.OUT)

                if GPIO.input(04) == GPIO.HIGH:
                        print("Pin 23 Button 2 was pushed")
                        GPIO.output(18,GPIO.HIGH)
                        time.sleep(1)
                        GPIO.output(18,GPIO.OUT)
                        print("2")
                else:
                        GPIO.output(18,GPIO.OUT)

        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)







# Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

# If we have the UID, continue
        if status == MIFAREReader.MI_OK:
                if Jeton_utiliser == str((uid_2_num(uid))):
                        # Turn on LED

                        GPIO.output(18,GPIO.HIGH)
                        GPIO.output(23,GPIO.HIGH)
                        GPIO.output(24,GPIO.HIGH)
                        GPIO.output(12,GPIO.HIGH)
                        GPIO.output(26,GPIO.HIGH)
#Turn LED off
                        time.sleep(1)
                        GPIO.output(12,GPIO.LOW)
                        GPIO.output(18,GPIO.LOW)
                        GPIO.output(23,GPIO.LOW)
                        GPIO.output(24,GPIO.LOW)
                        GPIO.output(26,GPIO.LOW)

#       myPID = os.getpid()
#       touchname = "touch /tmp/rfid." + str(myPID) + "." + str((uid_2_num(uid)))
#       subprocess.call(touchname , shell=True)
#               print str(uid_2_num(uid))
#               file = open("id.txt","w")
#               file.write(str(uid_2_num(uid)))
#               file.close()
#               continue_reading = False
#               GPIO.cleanup()



