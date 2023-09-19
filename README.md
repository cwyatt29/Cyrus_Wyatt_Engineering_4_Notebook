# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LED_blink.py](#led_blink)
* [LaunchPadPart1](#LaunchPadPart1)
* [LaunchPadPart2](#LaunchPadPart2)
* [LaunchPadPart3](#LaunchPadPart3)
* [LaunchPadPart4](#LaunchPadPart4)
* [CrashAvoidance1](#CrashAvoidanceSystem1)
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [Github_Intro](#Github_Intro)
&nbsp;


## led_blink

### Assignment Description
use vs code to make the onboard LED on the Rasberry Pi Pico blink.


### Evidence 
![Blink](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LED%20BLINK.gif)
### Wiring
No wiring was needed because the Pico has an onboard LED which can blink.
### Code

[Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/LED_blink.py)
### Reflection
This assignment was very simple most of the command scripts we needed were in the instructions so all that was needed was to order them correctly and run the code. This code would be useful if you want to make sure your pico is functioning properly before launching a rocket or another flying projectile.




## LaunchPadPart1

### Assignment Description
Create a code that will print a countdown into the serial monitor. Code should start at 10 and stop at 0.


### Evidence 
![Countdown](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Countdown%20GIf-min.gif)
### Wiring
No wiring was needed for this because it is only in a serial monitor
### Code


 [Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad/LaunchPadPart1)
### Reflection
The command N -= 1 is used to minus one from the value of N every loop. This is useful to know because N - 1 will just print 9 and N = -1 will print -1. Other than that the code is simple. Also remember to use if N = 0 break which will prevent the code from going into negative values.

## LaunchPadPart2

### Assignment Description
Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.


### Evidence 
![Lights](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/launchpad2.gif)
### Wiring
![Wires](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LaunchPad2Wiring.jpg)

### Code

 [Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad/LaunchPadPart2)

### Reflection
The Pico uses GP ports instead of D ports it is important to remember to name them as GP. The long leg of the LED is the positive side. The green LEDs are very hard to see when it is bright so I used a blue LED that shows up better.

## LaunchPadPart3

### Assignment Description
We need to add a button to our launch pad instead of using our code to begin the countdown. When the button is pressed we need to start the countdown. We don't have a saftey in place but we could make it so that if it is pressed again it will stop the countdown and reset it.


### Evidence 
![LaunchPad3](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LaunchPad3.gif)
### Wiring
![Wires](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LP3%20wiring.jpg)

### Code

 [Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad/LaunchPadPart3)

### Reflection
This was a good refresher for how button code works. This will be nice to look back at when we are making our projects later in the year. It is important to know whether you're pulling up or pulling down. Pull up means when you aren't pressing the button its seeing a true value. When you are Pulling down it means it will get a true value when the button is depressed. 

## LaunchPadPart4

### Assignment Description
Building off of the previous assignments, add a servo that rotates 180 degrees when the countdown reaches zero to mimic the movment of a support tower breaking away when launching a rocket.

### Evidence 
![LaunchPad4](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Launch%20Pad%204.gif)
### Wiring
![Wires](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LP4%20wiring.jpg)

### Code

[Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Launch%20Pad/LaunchPadPart4)

### Reflection
all of the commands we needed were already provided on canvas but its important to understand what they're actually doing. 
```python 
pwm_servo = pwmio.PWMOut(board.GP5, duty_cycle=2 ** 15, frequency=50) 
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)        
servo1.angle = 0                
```
the first line is defining the servo and telling the code which pin the servo is on. Duty cycle is the maximum frequency the servo will receive and frequency is the width of the pulses that the servo receives. The second line is making the 180 servo know that it can't go past a certain degree of rotation.

## CrashAvoidanceSystem1

### Assignment Description
We were assigned to code and wire an accelerometer that returns us its x, y, and z values in the serial monitor. This will be useful when we are doing our project because will will be able to look at our data and see how quickly our object moved. It would also be good for making a crash avoidance system.
### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Gyro1.gif)
### Wiring
![Wiring](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/CA1%20Wiring.jpg)
### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/Crash%20Avoidance%20Part%201)  
### Reflection
This assignment was fun for me because I got to use a sensor that I hadn't used before. It was a good refresher for using I2C which I had done before when using LCDs. Its important to note that the Z value is around 8.3 while the others are 0. this is because of the gravity of the earth which messes with the sensor causing it to not give us a 0.

## Raspberry_Pi_Assignment_Template
### Assignment Description
### Evidence 
### Wiring
![Wiring]()
### Code
[code]() **COMMENT YOUR CODE** 
### Reflection
## Onshape_Assignment_Template
### Assignment Description
### Part Link 
[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 
### Part Image
### Reflection
## Github_Intro
### Media Test
### Test Link
[testlink](https://www.google.com/search?q=matt+miller&rlz=1C1GCEU_enUS1072US1072&oq=matt+miller&gs_lcrp=EgZjaHJvbWUqDQgAEAAY4wIYsQMYgAQyDQgAEAAY4wIYsQMYgAQyCggBEC4YsQMYgAQyBwgCEAAYgAQyBwgDEC4YgAQyBwgEEAAYgAQyBwgFEC4YgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgyMzgzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&safe=active&ssui=on)
### Test Image 
### ![TEST](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/TEST.jpg)
### Test GIF
### ![testgif](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Testgif.gif)
