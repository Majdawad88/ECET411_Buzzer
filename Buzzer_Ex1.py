
# git clone https://github.com/Majdawad88/ECET411_Buzzer.git

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module GPIO.setwarnings(False) # Ign>
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
BUZZER_PIN = 23
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial val>

def BuzzerFreqControl(freq, time):
        print("Freq = "+ str(freq)+ " time = "+ str(time))
        if freq > 0:
                for i in range(int((freq)*time)):
                        GPIO.output(BUZZER_PIN, GPIO.HIGH)
                        sleep((1/freq)*0.5)
                        GPIO.output(BUZZER_PIN, GPIO.LOW)
                        sleep((1/freq)*0.5)
        else:

                sleep(time)

try:


        while True: # Run forever

                BuzzerFreqControl(250, 2)
                BuzzerFreqControl(500, 2)
                BuzzerFreqControl(750, 2)
                BuzzerFreqControl(0, 2)



except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



