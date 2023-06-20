
# import libraries
import RPi.GPIO as GPIO
import board
import adafruit_dht
from time import sleep

# declare pin
servoPin = 11
# create dht object
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

# set to use Broadcom GPIO numbers
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)
# set servo pin as output
GPIO.setup(servoPin, GPIO.OUT)
# initialize PWM on pin at 50Hz
pwm = GPIO.PWM(servoPin, 50)
# start pwm with 0 duty cycle so it doesn't set any angles on start
pwm.start(0)

# create function so we can call this later
def Set_Angle(angle):
    # calculate duty cycle from angle
    duty = angle / 18 + 2
    # turn on servo pin
    GPIO.output(servoPin, True)
    # set duty cycle to pin
    pwm.ChangeDutyCycle(duty)
    # wait 1s for servo to move into position
    sleep(1)
    # turn off servo pin
    GPIO.output(servoPin, False)
    # set duty cycle to 0 to stop signal
    pwm.ChangeDutyCycle(0)

Set_Angle(20)
sleep(1)
Set_Angle(40)
sleep(1)
Set_Angle(60)
sleep(1)
Set_Angle(80)
sleep(1)
Set_Angle(100)
sleep(1)
Set_Angle(120)
sleep(1)
Set_Angle(180)

    
# stop pwm on exit
pwm.stop()
# release GPIOs on exit
GPIO.cleanup()