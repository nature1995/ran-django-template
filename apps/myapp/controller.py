import time
import datetime
import Adafruit_DHT
import sys
import requests
import RPi.GPIO as GPIO
import sqlite3
import spidev

DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 24
GPIO.setmode(GPIO.BCM)
ROOM_SENSOR_PIN = 27
DOOR_SENSOR_PIN = 23
GPIO.setup(ROOM_SENSOR_PIN, GPIO.IN)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17
TRIGGER_PIN = 18
threshold = 10

def runController():
    now = datetime.datetime.now()
    dt = now.replace(microsecond=0)
    print(dt)
    print('Temperature: {0:0.1f} C'.format(tmp))
    print('Humidity:    {0:0.1f} %'.format(hmd))
    setDtState(dt)
    setTmpState(tmp)
    setHmdState(hmd)
    roomState = readingRoomSensor()
    pinState = readUltrasonicSensor()
    if roomState == 1:
        setRoomState('yes')
    else:
        setRoomState('no')
    doorState = readingDoorSensor()
    if doorState == 1:
        setDoorState('open')
    else:
        setDoorState('closed')
    if pinState == 1:
        print('On')
        setCurrentState('On')
    else:
        print('Off')
        setCurrentState('Off')


def setDtState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/dt/1/', data=values)


def setTmpState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/tmp/1/', data=values)


def setHmdState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/hmd/1/', data=values)


########################################################################
def readingRoomSensor():
    if GPIO.input(ROOM_SENSOR_PIN):
        print('motion detected')
        return 1
    else:
        return 0


def readingDoorSensor():
    if GPIO.input(DOOR_SENSOR_PIN):
        print('door opened')
        return 1
    else:
        return 0


def setRoomState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/room/1/', data=values)


def setDoorState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/door/1/', data=values)


########################################################################
def readUltrasonicSensor():
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)
    while GPIO.input(SENSOR_PIN) == 0:
        signaloff = time.time()
    while GPIO.input(SENSOR_PIN) == 1:
        signalon = time.time()
    timepassed = signalon - signaloff
    distance = timepassed * 17000
    if distance < threshold:
        return 1
    else:
        return 0


def setCurrentState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/state/1/', data=values)


while True:
    try:
        hmd, tmp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        if hmd is None or tmp is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(5)
    except KeyboardInterrupt:
        spi.close()
        GPIO.cleanup()
        exit()

