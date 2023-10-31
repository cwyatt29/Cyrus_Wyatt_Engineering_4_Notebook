
# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LED Blink](#LED-Blink)
* [Launch Pad Part 1](#Launch-Pad-Part-1)
* [LaunchPadPart 2](#Launch-Pad-Part-2)
* [LaunchPadPart 3](#Launch-Pad-Part-3)
* [LaunchPadPart 4](#Launch-Pad-Part-4)
* [Crash Avoidance Part 1](#Crash-Avoidance-System-Part-1)
* [Crash Avoidance Part 2](#Crash-Avoidance-System-Part-2)
* [Crash Avoidance Part 3](#Crash-Avoidance-System-Part-3)
* [Crash Avoidance Part 4](#Crash-Avoidance-System-Part-4)
* [FEA Beam Assignment Parts 1 & 2](#FEA-Beam-Assignment-Parts-1-&-2)
* [FEA Beam Assignment Part 3](#FEA-Beam-Assignment-Part-3)
* [FEA Beam Assignment Part 4](#FEA-Beam-Assignment-Part-4)
* [FEA Beam Assignment Part 5](#FEA-Beam-Assignment-Part-5)
* [Landing Area Part 1](#Landing-Area-Part-1)
* [Landing Area Part 2](#Landing-Area-Part-2)

&nbsp;
___

## LED Blink

### Assignment Description
use vs code to make the onboard LED on the Rasberry Pi Pico blink.


### Evidence 
![Blink](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/LED%20BLINK.gif)
### Wiring
No wiring was needed because the Pico has an onboard LED which can blink.
### Code

[Code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/LED_blink.py)
### Reflection
This assignment was very simple most of the command scripts we needed were in the instructions so all that was needed was to order them correctly and run the code. This code would be useful if you want to make sure your pico is functioning properly before launching a rocket or another flying projectile. I also added a switch to my wiring which isn't necessary but it makes it easier to turn on and off.


___

## Launch Pad Part 1

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
___
## Launch Pad Part 2

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
___
## Launch Pad Part 3

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
___
## Launch Pad Part 4

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
___
## Crash Avoidance System Part 1

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
___
## Crash Avoidance System Part 2

### Assignment Description

We needed to make a light turn on if our gyro is tilted at a 90 degree angle. We also had to make it so that our device would work without being powered from the computer. This is essentially a warning system, If our helicopter is at 90 degrees something is definitely wrong.

### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Gyro2.gif)
### Wiring
![Wiring](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/CA2%20Wiring.jpg)
### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/Crash%20Avoidance%20Part%202) 
### Reflection
I learned how to round values which is very useful and I wish that I had learned it sooner. This makes if statements so much easier and also makes it easy to look at data and read it. I also learned more about F strings which let us print things more easily. I had a refresher on and and or statements and when the right time to use them is.
___
## Crash Avoidance System Part 3

### Assignment Description
Add an onboard screen that will report values of angular velocity back to the pilot. We are using an OLED screen and wiring it through the same serial clock and serial data pins. We want to round these values because it will be simpler for the pilot to read while flying the helocopter.
### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Gyro3.gif)
### Wiring
![Wiring](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/CA3%20Wiring.jpg)
### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/Crash%20Avoidance%20Part%203) 


### Reflection
We got to use a new screen which I liked more than the LCD screens we had been using because this was able to print more information on one screen. The quality on the OLEDs is better than the LCD and you dont have to adjust the brightness on the device which is nice. This was the first time that I had two devices on one I2C which was important to learn because it lets me greatly condense my wiring and not run out of ports which I have done before on projects with lots of inputs and outputs.

___
## Crash Avoidance System Part 4

### Assignment Description
This was an optional assignment in which we were tasked with adding a altimeter to our crash avoidance system. If our system was above 3 meters the light would not come on. 
### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Gyro4.gif)

### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Crash%20Avoidance/Crash%20Avoidance%20Part%202) 

### Reflection
In this assignment we got to use a third sensor on the same I2C the altimeter, is a useful sensor because it can measure temp, altitude, and barometric pressure. This will be useful for our project later because it will let us measure differnt data. The sensor is also compact which is very important because we can't have a very heavy payload.
___
## FEA Beam Assignment Parts 1 & 2

### Assignment Description
Lucia Whitmore and I were tasked with making a 3d printed beam that could support the most weight. The parameters were that the beam had to hold the weight 180mm from the start of the beam, it couldn't weight more than 13g and it couldn't use any support material. Lucia and I started by brainstorming some ideas and researching bridges and cranes which had already achived the goal we were working towards. Next we both picked a design to work on and made it in OnShape, I choose to do a truss and Lucia made a triangle but switched to a box design because the triangle weighted far too much.
### Part Link 

[FEABEAM](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/bc14fcb1e64d92da7e0746b2?renderMode=0&uiState=651c47ac2c3aec7eb767df86)
### Part Image
<details>
  <summary>Images</summary>
 
   ![PartImage1](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Beam%20Starter%20%2B%20Holder%20Copy%201.png)
   ![PartImage2](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Beam%20Starter%20%2B%20Holder%20Copy%202.png)
</details>


### Reflection
I think that Lucia and I chose a good method of design which let us complete two different designs at the same time and more options mean more better. Lucias design was better than mine because she was able to make small adjustments which mine couldnt do as well. My design was more complicated than Lucias which meant it took more time to do and didn't necessarily make it any better. If I was going to do this again I wouldve started by making my original extrusion from the mounting peice more adjustable because that would have allowed me to cut the most weight quickly.
___
## FEA Beam Assignment Part 3

### Assignment Description

We were tasked with using onshape simulation tools to test our beams before printing them. By using the force tool we can simulate how our beam would react to having a weight on the end of it. This is useful for picking the best beam and for knowing where we need to make adjustments.


### Part Link 

[FEABEAM](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/bc14fcb1e64d92da7e0746b2?renderMode=0&uiState=651c47ac2c3aec7eb767df86)
### Part Image

<details>
  <summary>Part 1 Images</summary>
 
  #### Stress Image
  ![PartImage1a](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%201%20Simulation.png)
  #### Displacement Image
  ![PartImage1b](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%201%20Simulation%20Displacement.png)
  
</details>

#### Part 1 Analysis
To improve this design it would be good to remove material from the dark blue areas and add it to the red. This would involve removing parts off the side skirts and adding more to the spine that is close to the holder. There is the most stress there so it will also be good to use filets and chamfers to get rid of weak 90 degree points.

<details>
  <summary>Part 2 Images</summary
                         
  #### Stress Image
  ![PartImage2a](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%202%20Simulation%20Stress.png)
  #### Displacement Image
  ![PartImage2b](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Assembly%20Copy%202%20Simulation%20Displacement.png)
  
</details>

#### Part 2 Analysis
This design will need more changes than design 1. It would be benfitial to angle the fins to create more rigidity. It would be good to remove some material from the end of it and beef up the part close to the mounting point. If you look at the stress image you can see where it had the weakest point.


### Reflection
The FEA is very useful for this assignment, without it we would have to wait for our printers to print before we could test. This would also be more expensive than FEA. FEA will be useful in the future because we will be able to test different materials before we launch rockets or balloons. 

___
## FEA Beam Assignment Part 4

### Assignment Description
After completing part 3 we need to take what we learned and put it into our model. We are supposed to run multiple simulations after each change that we make to see if we have any improvement. Our design is pretty good right now but we will have to make small but important changes to the weak points to improve our design.

### Part Link 

[Part1Link](https://cvilleschools.onshape.com/documents/cebfb999b850e3304b183c8f/w/6d6994e08687c4d9aae8ad50/e/bc14fcb1e64d92da7e0746b2?renderMode=0&uiState=651c47ac2c3aec7eb767df86)
[Part2Link](https://cvilleschools.onshape.com/documents/68a3942f60c958fbf735b6e9/w/9c072b32744bb5fb1b10fb65/e/45140ff02c4b7573c4df0622)
### Part Image

####  Improvements
Because Lucia was out for most of the week we did this the main changes were all done by me but on the last day we decided to divide and conquere to see who could make a better design. As it turns out Lucia's design beat mine by a stress factor of 1 point so we decided to go with hers. Our maxium improvement was improved by a factor of 36.27% which is good considering that our design was already at a stress factor of 11.57.

<details>
  <summary>Part 1 Images</summary
                         

  #### Lucia's Stress Image
  ![Lucia's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%202%20stress.png)
  #### Lucia's Displacement Image
  ![Lucia's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%202%20displacement.png)
  
</details>
<details>
  <summary>Part 2 Images</summary
                         
  #### Cyrus's Stress Image
  ![Cyrus's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%201%20stress.png)
  #### Cyrus's Displacement Image
  ![Cyrus's Improvements](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Improved%20Beam%20copy%201%20displacement.png)
  
</details>
### Reflection

I had a hard time using the built in OnShape FEA tool because when I made upates it would take a long time for the simulation to tell me if it improved or not. I wish Lucia had been here for more time because we would've been able to improve our design a lot more. I Think that if we had more time I would have started a new design and remove the side peices because most of our strength came from our spine. We were able to get a single digit stress factor which I am happy with and I feel that we have a good chance of having one of the strongest beams in the class.
___
## FEA Beam Assignment Part 5

### Assignment Description

After breaking our beams we got to see where they would break in real life and we were tasked once again with improving our design. Lucia and I decided to scrap most of our last design because there were multiple issues with it.

### Part Link 

[Link1](https://cvilleschools.onshape.com/documents/68a3942f60c958fbf735b6e9/w/9c072b32744bb5fb1b10fb65/e/45140ff02c4b7573c4df0622)
### Part Image

<details>
  <summary>Part Images</summary
                     
![Stress Pic](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Third%20Try%20Stress%20Pic.png)
![Displacement Pic](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Thrid%20Try%20Displacement%20Pic.png)

</details>

####  Improvements

We kept the spine shape of it but instead of adding triangluar supports along the sides we added a long top beam that we chamfered so there was no overhangs where we would need support material. We also decided to add a support to the area where the beam slotted into the holder because many other teams had their parts break there and if we could fix the front portion where ours broke last time we should beef up the back too. We removed material using diamonds which were stronger than the square cut outs that we had used before. The most important change we made was making the head much bigger. We did this because on our last design it was extremely thin and snapped instantly. By making these changes we were able to get our stress factor down to 6.45 which is a 43% decrease from our original design.

### Reflection
If I was to do this again I would have trusted my intution over the FEA more. I also would have started over a lot sooner than I did because the originally design got to a point where it couldn't be any more improved. I am happy with the design that I have come up with and I think that when we break the beams this will perform better than my first design.


___
## Landing Area Part 1

### Assignment Description
We were tasked with making a code that could find the area of a triangle based off of 3 points. We were required to use functions and also needed the code to return an error instead of crashing if the wrong data was input (if you put a letter instead of a number). Data need to be input in the for (x,y) so you couldn't just do each point indivdually.
### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Landing%20Area%20GIFS/Landing%20Area%201%20Gif.gif)

### Wiring
There was no wiring for this assignment.

### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area/Part%201%20(Functions)) 
### Reflection

This assignement was more chalenging than previous assignments because we were learning skills that I had never done before. I liked doing this because I got to learn more about using math and logic and code. It was also useful to learn about try and except commands which would be very nice if we were making something where you have to input values. Without these it would cause the whole code to crash when data was input wrong. Making Our own functions is also very useful and a good way to make code more compact. This assignment could've been done without using functions but now that I know how to use them I wouldn't do it a different way.
___
## Landing Area Part 2

### Assignment Description
For this assignment we were tasked with adding a picture of our theoretical landing area onto our OLED screens. We would still input our 3 verticies and calculate the area and print the triangle and its area on the graph. Our area must be accurate for any input and our output should be displayed as kilometers squared.
### Evidence 
![Evidence](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/images/Landing%20Area%20GIFS/Landing%20Area%202%20GIF.gif)

### Wiring
![Wiring]()

### Code
[code](https://github.com/cwyatt29/Cyrus_Wyatt_Engineering_4_Notebook/blob/main/raspberry-pi/Landing%20Area/Part%202%20(Plotting)) 

### Reflection
This was a challenging assignment because the code that is used with OLED screens is fairly new to me. The wiring was very simple, only requiring the OLED and the PICO. I had issues because I would fail to index lists in the correct places which was very annoying becauses there are a lot of lists. Also in the begining I still had my inputs in the "try except" which caused the code to not let me bail out or save new code. To not have this problem only put the parts the could cause an error in the try except.  

<details>
  <summary>Hidden</summary
                     

## Raspberry_Pi_Assignment_Template
### Assignment Description
### Evidence 
![Evidence]()
### Wiring
![Wiring]()
### Code
[code]() 
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
</details>

