from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
from time import sleep

# Initialize I2C and SSD1306 display
i2c = I2C(1, scl=Pin(27), sda=Pin(26))
display = SSD1306_I2C(128, 64, i2c)

# Initialize HC-SR04 sensor
sensor = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=1000000)

# Initialize passive buzzer
buzzer = PWM(Pin(22))
buzzer.duty_u16(0)  # Turn off the buzzer initially

prev_distance = 0  # Variable to store the previous distance

while True:
    # Measure distance in centimeters
    distance = sensor.distance_cm()

    # Filter out distances above 400cm
    if distance > 400:
        continue

    print('Distance:', distance, 'cm')

    # Round the distance to two decimal places
    distance_rounded = round(distance, 2)

    # Clear display
    display.fill(0)

    # Show distance on the display
    display.text("Distance:", 0, 0)
    display.text(str(distance_rounded) + " cm", 0, 16)

    # Check distance and display appropriate message
    if distance < 15:
        display.text("Too close!", 32, 32)  # Centered text
        buzzer.freq(1500)  # Set buzzer frequency to 1500Hz
        buzzer.duty_u16(50000)  # Maximum duty cycle for maximum loudness
    elif 15 <= distance < 30:
        display.text("Close enough", 26, 32)  # Centered text
        buzzer.freq(1000)  # Set buzzer frequency to 1500Hz
        buzzer.duty_u16(int((30 - distance) * 8738) + 32767)  # Increase duty cycle as distance decreases
    elif distance >= 30:
        display.text("Keep going", 26, 32)  # Centered text
        buzzer.duty_u16(0)  # Turn off the buzzer

    display.show()

    # Stop the beep if the distance changes
    if distance != prev_distance:
        buzzer.duty_u16(0)  # Turn off the buzzer
        prev_distance = distance

    # Delay for a short period
    sleep(.5)
