# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
step_pins = [17,22,23,24]

# Set all pins as output
for pin in step_pins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

def reset():
  for pin in range(0, 4):
    xpin = step_pins[pin]
    GPIO.output(xpin, False)

def rotate(steps, delay, direction=1):

  step_count = len(seq)-1

  # Read wait time from command line
  if delay > 1:
    delay = int(delay)/float(1000)
  else:
    delay = 10/float(1000)

  # Initialise variables
  step_counter = 0

  # Start main loopwhile True:
  for i in range(0, 1024):
    for pin in range(0, 4):
      xpin = step_pins[pin]

      if seq[step_counter][pin]!=0:
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)

    step_counter += direction

    # If we reach the end of the sequence
    # start again
    if (step_counter >= step_count):
      step_counter = 0
    if (step_counter < 0):
      step_counter = step_count

    # Wait before moving on
    time.sleep(delay)

if __name__ == '__main__':
  rotate_motor(1024,5,1)
