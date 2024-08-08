# ESP32 Programming Box



## 1. Introduction

Based on ESP32, this programming box is a learning toolbox for children over 6 years old, as a shell wraps its circuit board, avoiding pins scratched children. 

The ESP32 programming box integrates 16 sensors and modules, including LED, button, 1.3 inch OLED display, photoresistor, sound sensor, speaker, temperature and humidity sensor as well as pressure sensor. Thus, the box can be matched with interesting experiments. In this tutorial, we provide 36 projects, like small lamp, automatic window, sound control light, compass, and environmental monitoring.

Each project contains two programming methods: MicroPython and KidsBlock Desktop graphical programming. The latter only need to build up code blocks so is conducive to the initial training of programming thinking.



## 2. Features

**1. No wiring:** We integrate wiring in circuit board, so no worry about the wrong wiring to burn the module.

**2. Multiple functions:** With ESP32 development board as control board, this box contains 16 sensors and modules, and it is available to either external 7-12V DC power or 6 AA batteries.

**3. Simple structure:** Ready-to-use and full shell package prevents hands from being scratched by pins and protects the board as well.

**4. Strong expansibility:** Four RJ11 interfaces are reserved beyond the shell, all of which are compatible with IIC communication.

**5. Basic programming learning:** Graphical programming for new hands to cultivate programming logic and foundation; MicroPython programming for developers to contact the underlying codes combined with hardware.



## 3. Parameters

**Operating voltage:** 3.3v

**External DC power:** 7-12V

**Built-in battery holder:** 9V (six AA batteries, of 1.5V each)

**USB power:** 5V

**Operating current:** 

**Operating temperature:** –10 °C ~ +65 °C



## 4. Kit List

| #    | PIC  | NAME                  | QTY  |
| ---- | ---- | --------------------- | ---- |
| 1    |      | ESP32 programming box | 1    |
| 2    |      | Type-c cable          | 1    |
| 3    |      | Key                   | 1    |
| 4    |      | IC card               | 1    |



## 5. Graphical Programming KidsBlock Desktop

<p style="color:red;">If you have never come into contact with KidBlock Desktop, please learn this section carefully.</p>

KidBlock Desktop tutorial: [KidsBlockDesktopInstallationAndUse.md](./KidsBlockDesktopInstallationAndUse.md)

Included: how to download and use KidsBlock Desktop.

## 6. Tutorial Download





## 7. ESP32 Programming Box

### 7.1 LED Blink

#### 7.1.1 Overview

LED Blink is one of the simplest entry-level programming projects. It only needs an LED and then upload the code on the Arduino IDE. This simple project helps beginners better master basic concepts.

#### 7.1.2 Schematic Diagram

![6-1-2](./media/6-1-2.png)

**LED lighting on:** The output current of the IO ports is limited, so the LED brightness may not be enough. Therefore, a NPN triode (Q2) is added to the circuit as a switch. We only need to add a high(low) level at the triode base pin 1 to light it up(out).

**Triode on/off:** To put it simple, when the base(pin 1) receives a high level, the collector(pin 3) and the transmitter(pin 2) are connected, so then VCC passes through the current-limiting resistor to the LED and then into the triode to GND, forming a loop. At this time, LED is on. When pin 1 receives a low level, pin 3 and 2 are disconnected so the current loop cannot be formed, resulting LED off.

#### 7.1.3 Code Blocks

1. ![j1](./media/j1.png) 

	The start of the execution of a code. Codes will not run without this block. The module blocks that need to be initialized should be added below the block.

2. ![j2](./media/j2.png) 

	Code run in here and are executing all the time (in a loop).

3. ![j3](./media/j3.png) 

	This block controls the ON/OFF of an LED. You only need to set the pin and power level(HIGH/LOW).

4. ![j4](./media/j4.png) 

	The delay seconds can be modified as needed. 

	Unit: s. 

	Some conversions: 1S=1000mS; 1mS=1000uS; For instance, if a delay of 10ms is required, input 0.01.

#### 7.1.4 Test Code

##### 7.1.4.1 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![image-led](./media/led.png), drag and put ![j3](./media/j3.png) block into ![j2](./media/j2.png). Set pin to IO23 and output to HIGH.

![6-1-4-1-2](./media/6-1-4-1-2.png)

4. In ![control](./media/control.png), add a delay ![j4](./media/j4.png) of 500ms. So we set it to 0.5s.

![6-1-4-1-3](./media/6-1-4-1-3.png)

5. Right-click ![j3](./media/j3.png) and you will see ![j5](./media/j5.png). Choose `Duplicate` and put the copy under ![6-1-4-1-4](./media/6-1-4-1-4.png):

![6-1-4-1-5](./media/6-1-4-1-5.png)

6. Modify ![j3](./media/j3.png) output into LOW.

![](./media/6-1-4-1-6.png)

##### 5.1.4.2 Test Result

After uploading code, the red LED will blink with an interval of 0.5 seconds.

#### 7.1.5 Extension

If you want the LED to blink more frequently, just modify the delay time in ![j4](./media/j4.png). If we set the time shorter, it will blink faster. Now let's set it to 0.25s.

##### 7.1.5.1 Text Code

**Directly open the code file we provide:**



**Manually build blocks:**

Build code blocks as above but set delay to 0.25.

![](./media/6-1-5-1-1.png)



##### 7.1.5.2 Test Result

After uploading code, the red LED will blink with an interval of 0.25 seconds. Compared to 7.1.4.1, it blinks more frequently.



### 7.2 Sound Sensor

#### 7.2.1 Overview

The sound sensor, with excellent sound reception, mainly contains a high sensitivity microphone and an LM358 operational amplifier. Weak sound signals are captured by the microphone and amplified by LM358, so the output is clear and recognizable, which can be effectively detected the sounds. 

This sensor features high sensitivity, fast response speed, so is widely used in sound detection and recognition, providing a stable and reliable voice input solution for various intelligent devices.

#### 7.2.2 Schematic Diagram

![6-4-2](./media/6-2-2.png)

**Working principle:** If the built-in electret film vibrates after receiving sounds, its capacitance will change to produce a tiny voltage. The LM358 chip is adopted in circuits to amplify the sound signals detected by the high-sensitivity microphone.

#### 7.2.3 Code Blocks

1. ![j12](./media/j12.png) 

	This block sets baud rate, generally 9600 or 115200. In this project, the baud rate is 9600 by default.

2. ![j13](./media/j13.png) 

	This block sets printing content on the monitor. There are three printing modes can be set: warp, no-warp, HEX(hexadecimal). **Warp** is the default mode. 

3. ![j14](./media/j14.png) 

	This module reads the analog value of the detected sound. 

#### 7.2.4 Test Code

##### 7.2.4.1 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![6-4-4-1-1](./media/6-2-4-1-1.png).

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), place ![j13](./media/j13.png) block into ![j2](./media/j2.png)
5. In ![sound](./media/sound.png), drag and put ![j14](./media/j14.png) into the content box of ![j13](./media/j13.png).

**Complete Test Code**

![6-2](./media/6-2-4-1-3.png)

##### 7.2.4.2 Test Result

After uploading code, the analog value of the sound will be printed on the serial monitor. Note that click ![6-2](./media/6-2-4-1-4.png) to set the baud rate before uploading code.

![6-2](./media/6-2-4-1-5.png)



### 7.3 PIR Motion Sensor

#### 7.3.1 Overview

The PIR motion sensor adopts RE200B-P element. 

Based on pyroelectric effect, the sensor is able to detect the infrared ray emitted by human body or animal. With Fresnel lens, it can even detect farther and wider. When a nearby human or animal motion is detected, the sensor outputs a high level.

####  7.3.2 Schematic Diagram

![6-3](./media/6-3-2.png)

**Working principle:** The human body maintains at 37 degrees, so it will emit a specific wavelength of about 10μm infrared. The sensor captures 10μM infrared to determine whether there is a motion.

#### 7.3.3 Code Blocks



#### 7.3.4 Test Code

##### 7.3.4.1 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**

1. ![j15](./media/j15.png) 

	This block reads PIR value. If a motion is detected, output 1. If not, output 0.

2. ![j16](./media/j16.png) 

	This block determines conditions. If the output is 1, execute code in "if"; If the output is 0, execute code in "else". 

**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.

2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).

3. In ![control](./media/control.png), drag ![j2](./media/j2.png).

	![6-4-4-1-1](./media/6-3-4-1-1.png)

![6-4-4-1-2](./media/6-3-4-1-2.png)

4. In ![control](./media/control.png), drag ![j16](./media/j16.png) into ![j2](./media/j2.png).

![6-3](./media/6-3-4-1-1.png)

5. In ![pir](./media/pir.png), find and put ![j15](./media/j15.png) into the condition box of ![j16](./media/j16.png). 

	Add the following block under "if": ![6-3](./media/6-3-4-1-2.png) prints “Someone!”; Add the following block under "else": ![6-3](./media/6-3-4-1-3.png) prints “No one!”

**Complete Test Code**

![6-3](./media/6-3-4-1-4.png)

##### 7.3.4.2 Test Result

After uploading code, when human motion is detected, the monitor prints “Someone!”; If not, it shows “No one!” (Note that click ![6-2](./media/6-2-4-1-4.png) to set the baud rate before uploading code to avoid garbled words.)

![6-3](./media/6-3-4-2.png)



### 7.4 Power Amplifier

#### 7.4.1 Overview

The 8002b power amplifier mainly consists of a speaker and an audio amplification chip. It can amplify small audio signals for about 8.5 times. These amplified sounds will be played through its speaker. Besides, it can also play some music or melodies. 

####  7.4.2 Schematic Diagram

![6-4](./media/6-4-2.png)

#### 7.4.3 Code Blocks

1. ![j17](./media/j17.png) 

	This block sets tones and durations to emit a certain sound of tone.

2. ![image](./media/j18.png) 

	This block integrates some songs so that you can directly use.

3. ![j19](./media/j19.png) 

	This block stops the play of tones.

#### 7.4.4 Test Code

##### 7.4.4.1 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![spk](./media/spk.png), set frequency to NOTE_C4 and duration to 500 in block![j17](./media/j17.png).
4. Similarly, add NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4
5. At last add a ![j19](./media/j19.png).

**Complete Test Code**

![6-4](./media/6-4-4-1-1.png)

##### 7.4.4.2 Test Result

After uploading code, the power amplifier plays Do, Re, Mi, Fa, So, La, Si, in a loop.

####  7.4.5 Extension

We make the module to play music.

##### 7.4.5.1 Test Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**

![6-4](./media/6-4-5-1.png)

##### 7.4.5.2 Test Result

After uploading code, the amplifier plays *Birthday Song*.



### 7.5 Photoresistor

#### 7.5.1 Overview

Photoresistor is photoelectric device that works according to semiconductor photoconductivity. It can be used to sense the brightness of the current environment to output a corresponding analog value.

####  7.5.2 Schematic Diagram

![6-5](./media/6-5-2.png)

Photoresistor takes advantage of the photoelectric effect of semiconductors. Its resistance varies with ambient light. 

In the light, the semiconductor material absorbs photon energy to produce electron-hole pairs, increasing the conductivity and reducing the resistance. The brighter the light is, the lower the resistance will be. From the changes of resistance, it can sense light intensity accurately. Therefore, it is widely used in automatic lighting, photoelectric control, real-time monitoring and regulation of light.

#### 7.5.3 Code Blocks

![j20](./media/j20.png) 

This block reads the analog value of the photoresistor.

#### 7.5.4 Test Code

##### 7.5.4.1 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![6-4-4-1-1](./media/6-2-4-1-1.png).

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), drag block ![j13](./media/j13.png) into ![j2](./media/j2.png)

5. In ![light](./media/light.png), find block ![j20](./media/j20.png) into the print box of ![j13](./media/j13.png)

6. At last, add a delay of 0.5s for better observing the results.

   

   **Complete Test Code**

   ![6-5](./media/6-5-4-1-1.png)

##### 7.5.4.2 Test Result

After uploading code, the serial monitor will print the analog value of the photoresistor. Cover the sensor with your hand, and you will see the value decreases. (Note that click ![6-2](./media/6-2-4-1-4.png) to set the baud rate before uploading code to avoid garbled words.)

![6-5](./media/6-5-4-2.png)



### 7.6 AD Button

#### 7.6.1 Overview

The AD button requires only one analog pin to read multiple button states, which greatly saves IO ports. It adopts analog acquisition, and the output voltages vary from pressed buttons, so that different analog values can be obtained. We can determine which button is pressed according to these values.

####  7.6.2 Schematic Diagram

![6-6-2](./media/6-6-2.png)

From the Schematic Diagram: 

When no button is pressed, the output at signal pin IO33 is pulled down by R34 (connected to GND. So the analog value of IO33 is 0, that is, low level 0V;

When button S1(the red button) is pressed, pin IO33 is connected to VCC. So the analog value of IO33 is 4095 (voltage = 3.3V).

When button S2(the yellow button) is pressed, the voltage of IO33 is that between R32 and R34: VCCxR34/(R32+R34) ≈ 2.2V, and the analog value is about 2432;

When button S3(the green button) is pressed, the voltage of IO33 is that between R32+R33 and R34: VCCxR34/(R32+R33+R34) ≈ 1.1V, and the analog value is about 1175.

#### 7.6.3 Code Blocks

1. ![j21](./media/j21.png) 

	This block reads the analog value of AD button module and determines which button is pressed according to this value.

2. ![j7](./media/j7.png) 

	This block declares variables. Its type is int by default. You can input a Name and an Assignment(initial value).

3. ![j8](./media/j8.png) 

	This block records a value of a variable so that we can directly use it to replace the value. Before using, you only need to modify its name into the needed variable.

4. ![j9](./media/j9.png) 

	This block assigns a value to a variable. For example, we need to assign 100 to variable val, just input the variable name and value in the block accordingly. 

5. ![j22](./media/j22.png) 

	This is a comparison block that compares the values on both sides. If the left one is greater than the right one, output 1; or else, output 0.

6. ![j23](./media/j23.png) 

	Similarly, this is also a comparison block. If the left one is lower than the right one, output 1; or else, output 0.

7. ![j24](./media/j24.png) 

	This is a logical block with two condition boxes. Only when both sides output 1, this block outputs 1. One or both of the two sides output 0, and this block will output 0.

8. ![j25](./media/j25.png) 

	This "if...then" block determines conditions. Put condition(s) in the diamond box to output 1 or 0 (as above introduced). If 1 is output, execute the following codes; If it is 0, do not execute. 

#### 7.6.4 Test Code

##### 7.6.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/variable.png), find and drag block ![j7](./media/j7.png) under ![6-4-4-1-1](./media/6-2-4-1-1.png).
4. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![](./media/j7.png)

![6-6](./media/6-6-4-1-1.png)

5. In ![control](./media/variable.png), put ![j9](./media/j9.png) into ![j2](./media/j2.png)

6. In ![adKey](./media/adKey.png), find ![j21](./media/j21.png) and put it into the variable name box in ![j9](./media/j9.png)

   ![6-6](./media/6-6-4-1-2.png)

5. In ![serial](./media/serial.png), place ![j13](./media/j13.png) under![6-6](./media/6-6-4-1-3.png)
6. In ![control](./media/variable.png), put ![j8](./media/j8.png) into![j13](./media/j13.png)
7. At last, add a delay of 0.3S for better observing results.

**Complete Test Code**

![6-6](./media/6-6-4-1-4.png)

##### 7.6.4.3 Test Result

After uploading code, the serial monitor will print the analog value of the module. When the red button is pressed, the value is about 4095, and the yellow is about 2432, and the green is about 1175. If no button is pressed, the value equals 0.

![6-6](./media/6-6-4-2.png)

####  7.6.5 Extension

##### 7.6.5.1 Code Flow

AD button logic table: 

|      Button       | the analog value of button being pressed | the analog value of button being released |
| :---------------: | :--------------------------------------: | :---------------------------------------: |
|  the red button   |                   4095                   |                     0                     |
| the green button  |                about 2432                |                     0                     |
| the yellow button |                about 1175                |                     0                     |

![6-6](./media/6-6-5-1.png)

##### 7.6.5.2 Test Code

Based on 7.6.4.1, we add a condition statement to determine the read analog value of AD button module so that we can tell which button is pressed.

![6-6](./media/6-6-4-1-4.png)

1. Remove block ![6-6](./media/6-6-5-2-1.png): just click **Delete**
2. In ![control](./media/control.png), put ![j25](./media/j25.png) under ![6-6](./media/6-6-5-2-9.png)
3. In ![operator](./media/operator.png), put ![j22](./media/j22.png) into the condition box of ![j25](./media/j25.png)

![6-6](./media/6-6-5-2-2.png)

4. In ![control](./media/variable.png), put ![j8](./media/j8.png)into the left part of ![j22](./media/j22.png), and input 3500 in the right: itme > 3500

![6-6](./media/6-6-5-2-3.png)

5. In ![serial](./media/serial.png), put ![j13](./media/j13.png) into the "if...then" block ![6-6](./media/6-6-5-2-3.png) and modify the printing content into “Red”, so as to determine whether the red button is pressed.

![6-6](./media/6-6-5-2-4.png)

6. In ![control](./media/control.png), drag ![j25](./media/j25.png) under ![6-6](./media/6-6-5-2-4.png)

7. In ![operator](./media/operator.png), put ![j22](./media/j24.png) into the condition box of ![j25](./media/j25.png)

8. In ![operator](./media/operator.png), find block ![j22](./media/j23.png), and put ![j8](./media/j8.png) in its left part and modify the right part to 3000:  item < 3000

9. In ![operator](./media/operator.png), find block ![j22](./media/j22.png), and put ![j8](./media/j8.png) in its left part and modify the right part to 3000:  item > 2000

10. Put ![6-6](./media/6-6-5-2-5.png) into ![j25](./media/j24.png) respectively. 

	Add a ![j13](./media/j13.png) under ![j25](./media/j25.png), and modify the printing content into “Green”.

![6-6](./media/6-6-5-2-6.png)

11. Duplicate ![image-6-6](./media/6-6-5-2-7.png) and modify 3000 to 1500, and 2000 to 100, and printing content into “Yellow”: 

![6-6](./media/6-6-5-2-8.png)

**Complete Test Code**

![6-6-5-2](./media/6-6-5-2.png)

##### 7.6.5.3 Test Result

After uploading code, the serial monitor will print the colors of the buttons. If one of the buttons is pressed, its color will be displayed: “Red”, “Green” or “Yellow”.

![6-6](./media/6-6-5-3.png)



### 7.7 Ultrasonic Sensor

#### 7.7.1 Overview

Ultrasonic sensor measures the distance of an object by sound waves. It boasts a transmitter and a receiver to emit sound waves and then measure the returned waves. The time difference between transmitting and receiving can be used to calculate the distance value. Beyond that, it is also used to detect the shape or presence of objects, build automatic doors, and measure flow rates and pressures.

####  7.7.2 Schematic Diagram

![6-7](./media/6-7-2.png)

**Working principle:** Like bats, the ultrasonic sensor sends an ultrasonic signal with a high frequency that human cannot hear. If these signals encounter obstacles, they will immediately reflect back and be received by the sensor. After that, the distance between the sensor and the obstacle is calculated according to the time difference between signals transmitting and receiving. 

**Maximum detection distance:** 3M

**Minimum detection distance:** 4cm

**Detection angle:** no greater than 15 degrees

#### 7.7.3 Code Blocks

![j26](./media/j26.png) 

This block reads the distance value. You can modify its unit into cm (default) or inch.

#### 7.7.4 Test Code

##### 7.7.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![6-4-4-1-1](./media/6-2-4-1-1.png)

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), put ![j13](./media/j13.png) in the block ![j2](./media/j2.png) and set the printing content to “Distance:” in no-warp mode.

![6-7](./media/6-7-4-1-1.png)

5. In ![serial](./media/serial.png), put ![j13](./media/j13.png) under the block ![image-20240628092544675](./media/image-20240628092544675.png)

4. In ![6-7](./media/ultrason.png), put ![j26](./media/j26.png) into the printing content of ![j13](./media/j13.png).

5. At last add a delay of 0.5S for better observing results.

**Complete Test Code**

![6-7](./media/6-7-4-1-2.png)

##### 7.7.4.2 Test Result

After uploading code, the serial monitor prints the distance values and refreshes them per second.

![6-7](./media/6-7-4-2.png)



### 7.8 NFC Sensor

#### 7.8.1 Overview

RFID-RC522 module adopts Phillips MFRC522 original chip in card reading circuit, which is easy to use and with low cost. It is suitable for equipment and reader development, advanced applications, RF card terminal design and producing.

####  7.8.2 Schematic Diagram

![6-8-2](./media/6-8-2.png)

**RFID (Radio Frequency Identification)**: 

The card reader is composed of a frequency transmitter module and a high level magnetic field. The Tag transponder is a device to be sensed without a battery. It consists only of tiny integrated circuit chips, media for storing data, and antennas for receiving and transmitting signals. To read the data in the tag, it must be placed within the reading range of the reader. After that, the reader will generate a magnetic field. According to Lenz's law (magnetic energy generates electricity), the RFID Tag will be powered, thus activating the device.

<p style="color:red;">NOTE: this module only recognize card working at 13.56MHz. It is recommended to use the provided card in the kit.</p>

#### 7.8.3 Code Blocks

1. ![j27](./media/j27.png) 

	This block initializes RFID module. Without it, its data cannot be read.

2. ![28](./media/j28.png) 

	This block reads the card value of the RFID sensor.

3. ![image-20240701104605293](./media/j29.png) 

	This is a comparison block that determines whether the value of two parts equals each other. When they are equal, it outputs 1, or else it outputs 0.

4. ![image-20240701104539284](./media/j30.png) 

	This is a logical block to reverse the value. That means this block outputs 0 when the condition block outputs 1, and it outputs 1 when the condition outputs 0. It reverses outputs. 

5. ![image-20240701104509861](./media/j31.png) 

	This is a conversion block that converts values into one of types of integer, decimal or string.

![image-20240701105332920](./media/j32.png)

#### 7.8.4 Test Code

##### 7.8.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![rfid](./media/RFID.png), find and put ![j27](./media/j27.png) under ![j1](./media/j1.png)
3. In ![serial](./media/serial.png), find ![j12](./media/j12.png) and set baud rate to 9600
4. In ![control](./media/variable.png), put ![j7](./media/j7.png) under ![6-4-4-1-1](./media/6-2-4-1-1.png), and set variable Type to `string`
5. In ![control](./media/control.png), put ![j2](./media/j2.png) below the block ![](./media/j7.png)

![image-20240701131338008](./media/6-8-4-1-2.png)

5. In ![control](./media/variable.png), place ![j9](./media/j9.png) in ![j2](./media/j2.png)

6. In ![rfid](./media/rfid.png), put ![j21](./media/j28.png) in the right box of block ![j9](./media/j9.png)

7. In ![control](./media/control.png), add a ![j25](./media/j25.png) under ![image-20240701131625149](./media/6-8-4-1-1.png)

8. In ![operator](./media/operator.png), put ![j22](./media/j30.png) into the condition box of ![j25](./media/j25.png)

9. In ![operator](./media/operator.png), put ![j22](./media/j29.png) into the condition box of ![j25](./media/j30.png)

![image-20240701131910235](./media/6-8-4-1-3.png)

10. In ![control](./media/variable.png), put ![j9](./media/j8.png) into the left part of ![j22](./media/j29.png)
11. In ![image-20240701132101678](./media/data.png), put ![j9](./media/j31.png) into the right part of ![j22](./media/j29.png) and modify the conversion value to “0” and conversion type to "string".

![image-20240701132257387](./media/6-8-4-1-4.png)

12. In ![serial](./media/serial.png), find ![j13](./media/j13.png) and put it into ![image-20240701132431720](./media/6-8-4-1-5.png), and modify the printing content into “RFID:” and set printing mode to no-warp.

13. Drag another ![j13](./media/j13.png), and then add a variable block ![j9](./media/j8.png) into the printing content box.

	As follows:

![image-20240701132734670](./media/6-8-4-1-6.png)

**Complete Test Code**

![image-20240701132810067](./media/6-8-4-1-7.png)

##### 7.8.4.2 Test Result

After uploading code, cover the RFID sensing area with the IC card or the key in the kit, and you will see the serial monitor prints the ID numbers.

![image-20240701133030371](./media/6-8-4-2.png)



### 7.9 Axis-X&Y Joystick Module

#### 7.9.1 Overview

Axis-X&Y Joystick is a high-precision input device for bidirectional control. Its X and Y axes are separated to control horizontal and vertical movements respectively. This module contains 10K resistance so that it ensures the stability and accuracy of signals. 

####  7.9.2 Schematic Diagram

![image-20240701134032989](./media/6-9-2.png)

ESP32 Axis-X&Y Joystick works based on a two-axis potentiometer that detects movements on two axes. When the joystick moves on axis X or Y, the resistance of the potentiometer changes, outputting analog voltage signals. After being received by ESP32 analog input pin (ADC), these signals will be read by ESP32 board and converted to digital values. Therefore, the joystick coordinate can be easily revealed during controlling. 

#### 7.9.3 Code Blocks

![image-20240701141348645](./media/j33.png) 

This block reads the values of Axis-X&Y Joystick module. You can set pins and axis.

#### 7.9.4 Test Code

##### 7.9.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/control.png), drag ![j2](./media/j2.png).![6-4-4-1-1](./media/6-2-4-1-1.png)

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), put ![j13](./media/j13.png) into ![j2](./media/j2.png), change printing content into “X:” and set to no-warp.

5. Add another ![image-20240701141959486](./media/6-9-4-1-1.png) and set to no-warp

6. In ![image-20240701141246757](./media/joy.png), find and drag block ![j14](./media/j33.png) into the printing content box of ![j13](./media/6-9-4-1-1.png) , set pin to IO35 and axis to X

   ![image-20240701142141328](./media/6-9-4-1-2.png)

7. Duplicate block ![image-20240701142500257](./media/6-9-4-1-3.png), and modify the printing content “X:” into “    Y:”(the two spaces separates the two values to be output). Change pin to IO39 and set axis to Y.

8. Add a delay of 0.3s for better observing results. 

   


**Complete Test Code**

![](./media/6-9-4-1-4.png)

##### 7.9.4.2 Test Result

After uploading code, the serial monitor prints the values on axis X and Y. Toggle the joystick, and these value changes. 

![image-20240701143706206](./media/6-9-4-2.png)



### 7.10 Temperature and Humidity Sensor

#### 7.10.1 Overview

AHT20 temperature and humidity sensor adopts I2C interface and 20Bit ADC, and its operating voltage is 2V-5V. It features small volume, stable performance and high precision (accuracy: temperature ±0.3℃, humidity ±2%RH). So it is widely used in smart home, consumer electronics, medical and automotive. The sensor is stable and can work in harsh environments.

####  7.10.2 Schematic Diagram

![image-20240701144311341](./media/6-10-2.png)

ATH20 temperature and humidity sensor transmits data via I2C interface, and it works according to resistive and capacitive technology. It detects the temperature because the material's conductivity changes with temperature, and it reflects humidity through the change in the capacitance value. The temperature measurement range is -40 ° C to +85 ° C with accuracy of ±0.3 ° C, and the humidity range is 0% ~ 100%RH ±2%RH. Besides, it features high accuracy, high reliability and long-term stability. With I2C protocol, ATH20 provides real-time and accurate temperature and humidity data under a variety of environmental conditions.

#### 7.10.3 Code Blocks

![image-20240702083642783](./media/j34.png) 

This block reads reads the temperature and humidity values. But it only reads one of them at once.

#### 7.10.4 Test Code

##### 7.10.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![serial](./media/serial.png), find ![j12](./media/j12.png) block and set baud rate to 9600, and put it under ![j1](./media/j1.png).
3. In ![control](./media/control.png), drag ![j2](./media/j2.png).![6-4-4-1-1](./media/6-2-4-1-1.png)

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), put ![j13](./media/j13.png) in ![j2](./media/j2.png), and set to print “T: ” in no-warp mode.

5. Add another ![image-20240701141959486](./media/6-9-4-1-1.png) and set to no-warp

6. In ![image-20240702084630903](./media/temp.png), put ![j14](./media/j34.png) into the printing box of ![j13](./media/6-9-4-1-1.png) to read “Temperature”.

   ![6-10](./media/6-10-4-1-1.png)

   

7. Duplicate ![6-10](./media/6-10-4-1-2.png) and change “T: ” into “    RH:”(the two spaces separates the two values to be output). Read “Humidity” value.

8. Add a delay of 1S for better observing the results.

**Complete Test Code**

![6-10-4-1-3](./media/6-10-4-1-3.png)

##### 7.10.4.2 Test Result

After uploading code,  the serial monitor prints temperature and humidity values and refreshes the results per second.

![6-10](./media/6-10-4-2.png)



### 7.11 Pressure Sensor

#### 7.11.1 Overview

BMP388 pressure sensor is a pneumatic MEMS sensor a very compact package, featuring small size, low power consumption but high performance. In brief, it is a combination of the temperature and pressure sensor, which is perfect for mobile applications. 

This module adopts proven piezoresistive pressure sensing technology with high accuracy and linearity, as well as long-term stability and high EMC stability. Besides, it maximize flexibility in multi-device working, and is ideal for altitude tracking in consumer electronics drones, wearables, smart homes, etc. 

As for improvement, we can optimize the device in terms of power consumption, resolution and filtering performance.

####  7.11.2 Schematic Diagram

![6-11](./media/6-11-2.png)

Based on piezoelectric pressure sensing technology, the BMP388 pressure sensor accurately measures pressure and temperature. It is capable of measuring air pressure in the 300 ~ 1250 hPa range without consuming much power (consuming only 3.4 µA at 1 Hz operating frequency). In addition, the built-in infinite impulse response filter can effectively reduce effects from external interference.

#### 7.11.3 Code Blocks

1. ![j35](./media/j35.png) 

	This block initializes the BMP388 pressure sensor. Without this block, the module will not work.

2. ![j36](./media/j36.png) 

	This block reads BMP388 sensor values. If the values are not read, they cannot be output.

3. ![j37](./media/j37.png) 

	This block outputs the values read by BMP388 sensor, including Pressure, Altitude and Temperature.

![j38](./media/j38.png)

#### 7.11.4 Test Code

##### 7.11.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![](./media/bmp388.png), find and put ![j35](./media/j35.png) under ![j1](./media/j1.png).
3. In ![serial](./media/serial.png), drag ![j12](./media/j12.png) and set baud rate to 9600, and put it under ![j35](./media/j35.png).
4. In ![control](./media/control.png), drag ![j2](./media/j2.png).![6-4-4-1-1](./media/6-2-4-1-1.png)

![6-2](./media/6-2-4-1-2.png)



4. In ![](./media/bmp388.png), put ![j13](./media/j36.png) in ![j2](./media/j2.png)

5. In ![serial](./media/serial.png), put ![j13](./media/j13.png) under![](./media/j36.png) and set to print “Pressure:” in no-warp mode.

   

7. Add one more ![image-20240701141959486](./media/6-9-4-1-1.png) block and set to no-warp

8. In ![](./media/bmp388.png), drag and put ![j14](./media/j37.png) block in the printing content of ![j13](./media/6-9-4-1-1.png) and set to show “Pressure:” values.

   ![6-11](./media/6-11-4-1-1.png)

9. Duplicate ![6-11](./media/6-11-4-1-2.png) and set to print “    Altitude:”(the two spaces separates the two values to be output). Modify to show data “Altitude”.

10. Duplicate ![6-11](./media/6-11-4-1-3.png) and set to print “      Temperature:” (the two spaces separates the two values to be output). Modify to show data “°C”.

11. Set ![6-11](./media/6-11-4-1-4.png) to print in warp mode.

12. Add a delay of 1S for better observing the results.

**Complete Test Code**

![6-11-4-1-5](./media/6-11-4-1-5.png)

##### 7.11.4.2 Test Result

After uploading code, the serial monitor prints the values read by BMP388 sensor.

![6-11](./media/6-11-4-2.png)



### 7.12 (Direction Recognition) Geomagnetic Sensor

#### 7.12.1 Overview

AK8975C geomagnetic sensor is a three-axis electronic compass IC with high sensitivity. It can output 13-bit data and accurately detect X, Y, Z axes geomagnetic values. Thus, it is suitable for portable devices with navigation function such as mobile phones and tablets.

####  7.12.2 Schematic Diagram

![6-12](./media/6-12-2.png)

The AK8975C geomagnetic sensor works in the principle of electromagnetic induction. It takes the Earth's magnetic field as a measurement benchmark to sense changes in the magnetic field through its internal magnetic material and coils. Specifically, when the magnetic material is affected by geomagnetic field, a directional constrained electron spin deflection will happen due to the field force, which in turn forms a magnetic field. This field induces potential signals in the coil.

This sensor amplifies and processes the induced potential signals, which are then transmitted to the system for further calculation, analysis and processing. So it measures geomagnetic magnetic field in the axis X, Y, and Z to determine the direction.

#### 7.12.3 Code Blocks

1. ![6-12](./media/j39.png) 

	This block is used to initialize AK8975 geomagnetic sensor.

2. ![j40](./media/j40.png) 

	This block reads the magnetic field direction.

3. ![j41](./media/j41.png) 

	This block reads the values on axis X, Y and Z: 

	![6-12](./media/j42.png)

#### 7.12.4 Test Code

##### 7.12.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![6-12](./media/compas.png), put ![j35](./media/j39.png) under ![j1](./media/j1.png)
3. In ![serial](./media/serial.png), drag ![j12](./media/j12.png) and set baud rate to 9600, and put it under ![j35](./media/j39.png)
4. In ![control](./media/control.png), drag ![j2](./media/j2.png).![6-4-4-1-1](./media/6-2-4-1-1.png)

![6-2](./media/6-2-4-1-2.png)

4. In ![serial](./media/serial.png), put ![j13](./media/j13.png) in ![](./media/j2.png) and set to print “X:” in no-warp mode.

   

5. Add a ![image-20240701141959486](./media/6-9-4-1-1.png) and set to no-warp mode.

6. In ![](./media/compas.png), put ![](./media/j41.png) into the printing content of ![j13](./media/6-9-4-1-1.png), and set to read axis “X”.

   ![6-12](./media/6-12-4-1-1.png)

7. Duplicate ![6-12](./media/6-12-4-1-2.png) and change to read “    Y:”(the two spaces separates the two values to be output). Set to read value in axis “Y”.

8. Duplicate ![6-12](./media/6-12-4-1-3.png)and change to read “      Z:”(the spaces separates the two values to be output). Set to read value in axis “Z”.

9. Duplicate ![6-12](./media/6-12-4-1-4.png)and change to read “        Direction:”(the spaces separates the two values to be output).

10. In ![](./media/compas.png), put ![](./media/j40.png) into the printing content of ![j13](./media/6-9-4-1-1.png) and set mode to warp.

11. Add a delay of 1S for better observing the results.

**Complete Test Code**

![6-12-4-1-5](./media/6-12-4-1-5.png)

##### 7.12.4.2 Test Result

After uploading code, the serial monitor prints the sensor values. Move the programming box to see the changes of these values.

![6-12](./media/6-12-4-2.png)



### 7.13 Fan/Motor Module

#### 7.13.1 Overview

The motor adopts HR1124S motor control chip that is a single channel H-bridge driver chip used in DC motors. The H-bridge drive uses PMOS and NMOS power tubes with low on-resistance, ensuring lower power loss and longer safe working time. In addition, its standby and static working current are both low, so it is commonly used in toys.

####  7.13.2 Schematic Diagram

![6-13](./media/6-13-2.png)

**Motor control logic table:**

| IO18 | IO17 |      motor state      |
| :--: | :--: | :-------------------: |
| HIGH | LOW  |    forward rotate     |
| LOW  | HIGH |    reverse rotate     |
| HIGH | HIGH | stop (a gradual stop) |
| LOW  | LOW  | brake (a brake stop)  |



#### 7.13.3 Code Blocks

![6-13](./media/j44.png) 

This block controls the rotation of the motor. You only need to set motor pins and output levels of the pins.

#### 7.13.4 Test Code

##### 7.13.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![motor](./media/motor.png), put ![6-13](./media/j44.png) into ![j2](./media/j2.png), and set pin IO17 to output `LOW` and pin IO18 to output `HIGH`.
4. Add a delay of 2S.

![6-13](./media/6-13-4-1-1.png)

5. Duplicate the above code and modify pin IO17 to `HIGH` and IO18 to `LOW`.
6. Duplicate again and set both IO17 and IO18 to `LOW`.

**Complete Test Code**

![6-13](./media/6-13-4-1-2.png)

##### 7.13.2 Test Result

After uploading code, you will see the fan forward rotates for 2s and then reverses for another 2s. Then it stops. These actions repeat.



### 7.14 Servo

#### 7.14.1 Overview

The 9g servo features small size but high performance and precision and is with good torque and accuracy, so it is perfect for small machines. With up to 180 degrees rotation angle, it enables extremely precise rotation and control and can be started fast with low noise.

####  7.14.2 Schematic Diagram

**Angle range:** 180°(there are 360°, 180° and 90°)

**Drive voltage:** 3.3V / 5V

Usually three wires:

![6-14](./media/6-14-2-1.png)

**GND:** grounded, in brown

**VCC:** connect to +5v (3.3V) power, in red

**S:** signal pin to control PWM signal, in orange

![6-14](./media/6-14-2-2.png)

**Control principle**: The rotation Angle of the servo is controlled by adjusting the duty cycle of the PWM (pulse width modulation) signals. Theoretically, the period of the standard PWM signal is fixed at 20ms (50Hz), so the pulse width should be 1ms ~ 2ms. But in fact, it is 0.5ms ~ 2.5ms, corresponding to the servo angle of  0° ~ 180°. Note that the angle for the same signal varies from servo brands.

#### 7.14.3 Code Blocks

1. ![j43](./media/j43.png) 

	This block controls servo angle. You only need to set a pin, channel, degree(range of 0-180) and delay(1000=1S).

2. ![j45](./media/j45.png) 

	This block reads servo angle.

3. ![j6](./media/j6.png) 

	This is a repeat block with repeating times. You can set the times. For instance, here it is 10, so codes in it will repeatedly execute for 10 times.

#### 7.14.4 Test Code

##### 7.14.4.1  Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![servo](./media/servo.png), put ![j43](./media/j43.png) in block ![j2](./media/j2.png) and set degree to “0” and delay to “2000”.
4. Duplicate the block twice and set degree to “90” and “180” respectively.

**Complete Test Code**



![](./media/6-14-4-1.png)

##### 7.14.4.2 Test Result

After uploading code, the servo rotates to 0 degree, 90 degree and 180 degree accordingly, with each each position staying for 2 seconds, and then it back to 0 degree. It repeats these rotations.

####  7.14.5 Extension

We control servo to repeatedly and gradually rotate from 0 degree to 180 degree and then gradually back to 0 degree.

##### 7.14.5.1 Test Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![variable](./media/variable.png), drag ![j7](./media/j7.png) and put it under ![j1](./media/j1.png)

![6-18](./media/6-18-3-2-1.png)

4. In ![control](./media/control.png), drag ![j6](./media/j6.png) to set times to 180, and put it into ![j2](./media/j2.png)
5. In ![variable](./media/variable.png), put ![j10](./media/j10.png)into ![6-14](./media/6-14-4-1-2.png)

![6-14](./media/6-14-4-1-3.png)

6. In ![](./media/servo.png), drag and put ![](./media/j43.png) under ![j10](./media/j10.png)

7. In ![variable](./media/variable.png), set ![j8](./media/j8.png) to the degree in block ![](./media/j43.png), and set delay to 10 (unit: ms)

   ![6-14](./media/6-14-4-1-1.png)

   

8. Duplicate ![6-18](./media/6-14-4-1-2.png) and change “++” into “- -” in![j10](./media/j10.png)

**Complete Test Code**

![6-14](./media/6-14-4-1-4.png)

##### 7.14.5.1 Test Result

After uploading code, the servo repeatedly and gradually rotates from 0 degree to 180 degree and then gradually back to 0 degree.



### 7.15 WS2818 RGB LED

#### 7.15.1 Overview

WS2812 RGB LED is an external control LED integrating control circuit and light emitting circuit. It adopts single-line return-to-zero code communication, and supports 256 gray levels to display full-colors. The integrated chip inside each pixels efficiently stabilizes color output. So it is widely used in lighting, display and decoration.

####  7.15.2 Schematic Diagram

![6-15-2](./media/6-15-2.png)

From the Schematic Diagram, ws2812 connects and transmits data over a single wire, which is the communication method named single-bus return-to-zero code (single NZR). The data enters in serial through the DIN port, and each pixel receives and processes 24 bits data (R, G, B color channels with 8 bits each). 

For detailed information of transmission mode, please refer the specification of ws2812.

#### 7.15.3 Code Blocks

1. ![6-15](./media/j46.png) 

	This block initialize the ws2812 module. You only need to set its numbers and pin.

2. ![j47](./media/j47.png) 

	This module appoints one certain ws2812 pixel to light up. You only need to input the ws2812 pixel number (starting from 0) and set its color.

3. ![j48](./media/j48.png) 

	This block appoints a certain range of ws2812 pixels to light up. You only need to input two ws2812 pixel number (a starting and a ending pixel)  and set their colors.

4. ![j49](./media/j49.png) 

	This block sets colors of the LED. Three parameters (R, G, B) should be set. 

5. ![image-j50](./media/j50.png) 

	This block sets the brightness of ws2812 pixels. Its range is 0 ~ 255.

6. ![image-j51](./media/j51.png) 

	This block turns off all ws2812 pixels.

7. ![j52](./media/j52.png) 

	This block refreshes the state of each ws2812 pixel. Before every part that controls pixels, this block should be added after them. Otherwise, they are invalid settings.

#### 7.15.4 Test Code

##### 7.15.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![](./media/RGB.png), find and put ![6-15](./media/j46.png) under![j1](./media/j1.png)
3. In ![](./media/RGB.png), put ![6-15](./media/j50.png) under![j1](./media/j46.png) and set brightness to 50 to avoid glaring.
4. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![6-15](./media/j50.png)

![6-15](./media/6-15-4-1-1.png)

5. In ![](./media/RGB.png), put ![j47](./media/j47.png) into ![j2](./media/j2.png), and set pixel to 0 and color to red. 
6. In ![](./media/RGB.png), add a ![j47](./media/j52.png) to refresh the above settings so that ws2812 will light up.

**Complete Test Code**

![6-15](./media/6-15-4-1-2.png)

##### 7.15.4.2 Test Result

After uploading code, the first pixel of ws2812 lights up in red.

#####  7.15.5 Extension

Light up all LED circulating red, green, and blue.

##### 7.15.5.1 Test Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![RGB](./media/RGB.png), drag and put ![6-15](./media/j46.png) under ![j1](./media/j1.png)
3. In ![RGB](./media/RGB.png), drag and put ![6-15](./media/j50.png) under ![j1](./media/j46.png), and set brightness to 50 to avoid glaring.
4. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![6-15](./media/j50.png)

![6-15](./media/6-15-4-1-1.png)

5. In ![RGB](./media/RGB.png), put ![j47](./media/j48.png) in ![j2](./media/j2.png), and set to fill pixel from “0” to “11”, and modify the color to red.
6. In ![RGB](./media/RGB.png), add a ![j47](./media/j52.png) to refresh the above settings so that ws2812 will light up.
7. Add a delay of 1S.

![6-15](./media/6-15-5-1-1.png)

8. Duplicate ![6-15](./media/6-15-5-1-2.png) and set the color to green.
9. Duplicate again ![6-15](./media/6-15-5-1-3.png) and set the color to blue. 

**Complete Test Code**

![6-15-5-1](./media/6-15-5-1.png)

##### 7.15.5.2 Test Result

After uploading code, ws2812 repeatedly lights up in red, green and blue with 1s each.



### 7.16 OLED Display

#### 7.16.1 Overview

OLED display is also called organic light-emitting diode or organic dot laser display. This display is self-luminous. It adopts a very thin coating of organic materials and glass substrate which will light up if current passes through. Therefore, it does not require a back-light. Note that it will not light up when just powering on; programing and wiring are also needed.

Besides, it features large viewing Angle, low power consumption, high contrast, thin display, fast response, simple structure, and can work on flexion boards within a wide temperature range.

####  7.16.2 Schematic Diagram

Communication mode: I2C communication

Internal driver chip: SSD1306

Resolution: 128 x 64





#### 7.16.3 Code Blocks

1. ![](./media/j53.png) 

	This block initializes OLED display, which is necessary when using OLED module.

2. ![](./media/j54.png) 

	This block sets size and color of the displayed text. The default settings are usually used.

3. ![](./media/j55.png) 

	This block sets the position of text starting to be displayed on the OLED.

4. ![](./media/j56.png) 

	This block inputs the printing text on OLED, and only strings are available. 

5. ![QQ_1721202190912](./media/j57.png) 

	This block displays icons. Some commonly used icons are integrated in this block.

6. ![](./media/j58.png) 

	This block clears all text on OLED.

7. ![](./media/j59.png) 

	This block refreshes OLED display. This block should be added after your settings. Otherwise, they are invalid.

8. ![QQ_1721202248225](./media/j60.png) 

	This block shows scrolling text on the display. You can set the scrolling direction.

9. ![QQ_1721202264020](./media/j61.png) 

	This block stops the scrolling of the text.

#### 7.16.4 Test Code

##### 7.16.4.1 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.

2. In ![](./media/oled.png), find and put ![](./media/j53.png) and ![](./media/j54.png) under ![j1](./media/j1.png) in sequence.

3. Add ![](./media/j58.png) under ![](./media/j54.png)

4. In ![control](./media/control.png), put ![j2](./media/j2.png) under ![](./media/j58.png)

5. Put ![](./media/j55.png) into ![j2](./media/j2.png)

6. Add a ![](./media/j56.png) under ![](./media/j55.png), and you can modify the text into whatever you like.

7. Put ![](./media/j59.png) under ![](./media/j56.png)

**Complete Test Code**

![QQ_1721353998374](./media/6-16-4-1.png)

##### 7.16.4.2 Test Result

After uploading code, you will see the OLED shows the text you set. Here we maintain it as default, so it displays “Hello KidsBlock”, as shown below:

![6-16-4-2](./media/6-16-4-2.png)

####  7.16.5 Extension

Scroll text on OLED display.

##### 7.16.5.1 Test Code

Open code “6-16-4-1”, and we make some changes on it:

1. Drag and put ![QQ_1721202248225](./media/j60.png)under ![](./media/j53.png), and set y1 to “64”.
2. Remove block ![](./media/j59.png). If it keeps refreshing, the text strings will not scroll.

**Complete Test Code**

![QQ_1721354861079](./media/6-16-5-1.png)

##### 7.16.5.2 Test Result

After uploading code, you will see the text is scrolling to right on the display. 



### 7.17 Traffic Light

#### 7.17.1 Overview

The traffic light module limits the pedestrian and vehicular thoroughfare. It includes a red, a yellow and a green light, which imply different instructions.

**Red for Stop:** Pedestrians and vehicles stop proceeding.

**Yellow for Caution:** Pedestrians and vehicles are ready for stopping. If the drive is already in process, the speed should be slow.

**Green for Proceed:** Pedestrians and vehicles keep going with the abidance of traffic regulations.

In this project, you can program on Arduino development board to control a mini traffic light. For instance, set the duration of each lights and the interval time among them. Besides, you may also add a timer to alter light colors to schedule.

#### 7.17.2 Test Code

##### 7.17.2.1 Code Flow

![6-17](./media/6-17-3-1.png)

##### 7.17.2.2 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![image-led](./media/led.png), find and put ![j3](./media/j3.png) into ![j2](./media/j2.png) and set pin to IO27 and output HIGH.

![6-17](./media/6-17-3-2-1.png)

4. In ![control](./media/control.png), add a ![j4](./media/j4.png) and set to 5S. And set pin to IO27 to output LOW on block ![j3](./media/j3.png).

![6-17](./media/6-17-3-2-2.png)

5. In ![control](./media/control.png), find ![j6](./media/j6.png) and set repeating times to 3, place it under ![6-17](./media/6-17-3-2-3.png)

![6-17](./media/6-17-3-2-4.png)

6. Build code in ![6-17](./media/6-17-3-2-5.png) to make yellow LED blink with an interval of 0.5s:![6-17](./media/6-17-3-2-6.png)

![6-17](./media/6-17-3-2-7.png)

7. Build code under ![6-17](./media/6-17-3-2-5.png) to make red LED light up for 5S then go off.

![6-17](./media/6-17-3-2-8.png)

**Complete Test Code**

![6-17-3-2](./media/6-17-3-2.png)

##### 7.17.2.3 Test Result

After uploading code, the green LED lights up for 5s and goes off. Immediately, the yellow LED blinks for three times. After that, the red LED lights up for 5s and goes off. These actions are exactly a model of traffic light and will repeat. 



### 7.18 Breathing LED

#### 7.18.1 Overview

PWM breathing LED utilizes on-board programmable PWM to output analog waveform. After powering on, LED brightness can be adjusted through duty cycle of the waveform to eventually realize a breathing light.

In this way, ambient light can be simulated by changing LED brightness along with time. Also, breathing LED can form a colorful mini light show to construct a tranquil and warm environment.

#### 7.18.2 Working Principle

PWM controls analog output via digital means, which are able to adjust the duty cycle of the wave (a signal circularly shifting between high level and low level).

For Arduino, digital ports of voltage output are LOW and HIGH, which respectively correspond to 0V and 5V. Generally, we define LOW as 0 and HIGH as 1. Arduino will output 500 signals of 0 or 1 within 1s. If they are 500 “1”s, 5V will be output. Oppositely, if they are all 0s, the output will be 0V. Or if they are 010101010101…, the average output will be 2.5V. In other words, output ratio of 0 and 1 affects the voltage value. 

Honestly, it differs from real continuous output, yet the more 0 and 1 signals are output per unit time, the more accurate the control will be.

![6-18](./media/6-18-2.png)

#### 7.18.2 Code Blocks

1. ![j10](./media/j10.png) 

	This block will increase or decrease one on the value of the variable when it is execute each time. The variable name can be set. There are ++ and – – can be chosen: ++ add 1; – – minus 1.

2. ![1](./media/j11.png) 

	This block the brightness of the LED. You need to set LED pin, channel and analog value of brightness(ranging from 0-255).

#### 7.18.3 Test Code

##### 7.18.3.1 Code Flow

![6-18](./media/6-18-3-1.png)

##### 7.18.3.2 Build Code

There are two ways to upload the code: directly open the code file we provide; or manually build blocks.

**Directly open the code file we provide:**



**Manually build blocks:**

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![variable](./media/variable.png), drag block ![j7](./media/j7.png) (keep the default) and put it under ![j1](./media/j1.png)

![6-18](./media/6-18-3-2-1.png)

4. In ![control](./media/control.png), drag ![j6](./media/j6.png) and set times to 255, put it in ![j2](./media/j2.png)
5. In ![variable](./media/variable.png), put ![j10](./media/j10.png) in ![6-3-3-2-2](./media/6-18-3-2-2.png)

![6-18](./media/6-18-3-2-3.png)

6. In ![](./media/led.png), put ![](./media/j11.png) under ![j10](./media/j10.png)

7. In ![variable](./media/variable.png), find ![j8](./media/j8.png) and do not need to modify the name, put it in the analog value of ![](./media/j11.png). 

7. Add a delay of 0.01S.

   ![6-18](./media/6-18-3-2-4.png)

   

8. Duplicate ![6-18](./media/6-18-3-2-2.png), modify ++ in ![j10](./media/j10.png) into – –.

**Complete Test Code**

![6-18](./media/6-18-3-2-5.png)

##### 7.18.3.3 Test Result

After uploading code, the red LED gradually lights on and dims out, in a circulation. It “breathes” evenly.



### 7.19 Button Control LED

#### 7.19.1 Overview

In this project, we control the ON/OFF of the LED via an AD button. The LED will light up if we press the button and it goes off when we press the button again.

#### 7.19.2 Test Code

##### 7.19.2.1 Code Flow



![6-19-2-1](./media/6-19-2-1.png)

##### 7.19.2.2 Build Code

1. In ![events](./media/events.png), find ![j1](./media/j1.png) block.
2. In ![control](./media/control.png), find and place ![j2](./media/j2.png) block under ![j1](./media/j1.png).

![6-1-4-1-1](./media/6-1-4-1-1.png)

3. In ![variable](./media/variable.png), find ![j7](./media/j7.png) and put it under ![j1](./media/j1.png), name the variable to “item“ and assign to “1” as its initial value.

![6-19](./media/6-19-2-2.png)

4. In ![control](./media/control.png), put ![j25](./media/j25.png) into ![j2](./media/j2.png).
5. In ![operator](./media/operator.png), find and put ![j22](./media/j22.png) into the condition box of ![j25](./media/j25.png)

![6-19](./media/6-19-2-2-3.png)

4. In ![](./media/adkey.png), find ![j8](./media/j21.png) and put it in the left part of ![j22](./media/j22.png), and set the right part to value 3500: AD key analog value > 3500

![6-19](./media/6-19-2-2-4.png)

5. In ![control](./media/control.png), find and put block ![](./media/j16.png) into ![6-19](./media/6-19-2-2-4.png).
6. In ![operator](./media/operator.png), put ![j29](./media/j29.png) into the condition box of ![](./media/j16.png)
7. In ![variable](./media/variable.png), put ![j8](./media/j8.png) into the left part of the ![j29](./media/j29.png), and modify the right part into “1”: variable item = 1

![6-19](./media/6-19-2-2-5.png)

8. In ![](./media/led.png), drag and put ![](./media/j3.png) in "if" of block ![6-19](./media/6-19-2-2-6.png)
9. In ![variable](./media/variable.png), put ![j8](./media/j9.png) under ![](./media/j3.png)
10. Duplicate ![](./media/j3.png) and put into "else" of block ![6-19](./media/6-19-2-2-7.png), and set LED to output “LOW” and set item variable by “1”.
11. Add a delay of 0.3s below ![](./media/j16.png).

**Complete Test Code**

![6-19-2-2-8](./media/6-19-2-2-8.png)

##### 7.19.2.3 Test Result

After uploading code, press the red button and the red LED lights up; press it again and the LED goes off.



### 7.20 Intrusion Alarm

#### 7.20.1 Overview

Intrusion alarm is a device alerting illegal intrusion into a prevention area. It plays an important role in security. We can see it everywhere: families, stores, warehouses, supermarkets and so on. 

All in all, it protects our personal and property safety.

#### 7.20.2 Test Code

##### 7.20.2.1 Code Flow

![6-20-2-1-2](./media/6-20-2-1-2.png)

##### 7.20.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. ![](./media/j16.png) 

	We use this block to determine the PIR motion sensor value. When the sensor outputs 1, the speaker alarms, the red LED turns on and the green one is off. If the sensor value equals 0, the red LED will go off and the green will be on; at the same time, the speaker stays quiet. 

**Complete Test Code**

![6-20](./media/6-20-2-2.png)

##### 7.20.2.3 Test Result

After uploading code, when the sensor detects a motion around, the speaker alarms, the red LED turns on and the green one is off. If no intrusion is detected, the red LED will go off and the green will be on; at the same time, the speaker stays quiet. 



### 7.21 Window Close In Dark

#### 7.21.1 Overview

In this project, we program to make the window automatically close when getting dark. So the photoresistor is required to sense the ambient light. We set a threshold for the resistor. When ambient light value is lower than the threshold, the servo closes the window. 

#### 7.21.2 Test Code

##### 7.21.2.1 Code Flow

![6-21-2-1](./media/6-21-2-1-1.png)



##### 7.21.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. We add ![](./media/j16.png) to determine the photoresistor value. If the analog value is lower than 500, the servo will rotate to 180 degree. If not, servo will rotate to 0 dgree.

**Complete Test Code**

![6-21](./media/6-21-2-1.png)

##### 7.21.2.2 Test Result

After uploading code, cover the photoresistor with something, and the servo will rotate to 180 degree. Remove the cover, and the analog value exceeds 500, so the servo rotates to 0 degree.



### 7.22 Voice Control Light

#### 7.22.1 Overview

Voice-control-light device mainly consists of a sound sensor, a photoresistor and an LED. The photoresistor is adopted to avoid LED lighting up during daytime. The sound sensor measures sound volume to determine whether it is reached the set threshold. If yes, the LED will light up for a few seconds. 

#### 7.22.2 Test Code

##### 7.22.2.1 Code Flow

![6-22-2-1](./media/6-22-2-1.png)

##### 7.22.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. Drag ![j25](./media/j25.png) to determine the photoresistor value. If it is lower than 500 (light < 500), execute its following code blocks.

![6-2](./media/6-22-2-2-1.png)

3. Add a ![j25](./media/j25.png) again to determine the sound sensor value. If the value is greater than 200 (sound > 200), execute its following code blocks. 

![6-22](./media/6-22-2-2-2.png)

4. When sound > 200, red LED lights up and then goes off after 5 seconds.

![6-22](./media/6-22-2-2-3.png)

**Complete Test Code**

![6-22](./media/6-22-2-2-4.png)

##### 7.22.2.3 Test Result

After uploading code, the LED never lights up no matter how loud the noise you make. Cover the photoresistor, and make some sounds, and you will see the LED light up for 5 seconds. 



### 7.23 Human Body Piano

#### 7.23.1 Overview

The analog piano mainly includes an ultrasonic sensor to detect the distance of your position. It plays different tones according to distance values. If there is an open space, you may place it on ground to play musics.

#### 7.23.2 Test Code

##### 7.23.2.1 Code Flow

![6-23-2-1](./media/6-23-2-1.png)

##### 7.23.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. Declare a variable and name to *distance*
3. Assign the detected value by the ultrasonic sensor to *distance*

![QQ_1721810318114](./media/6-23-2-2-1.png)

2. Add a ![j25](./media/j25.png) to determine the value of *distance*. If **distance > 5 and distance < 10**, the speaker will play Tone Do.

![QQ_1721810602031](./media/6-23-2-2-2.png)

3. Duplicate the above code blocks, and modify the condition to **distance > 10 and distance < 15**. Under this condition, the speaker plays Re.

![QQ_1721810782920](./media/6-23-2-2-3.png)

4. Duplicate the above code blocks, and modify the condition to **distance > 15 and distance < 20**. Under this condition, the speaker plays Mi.
5. Duplicate the above code blocks, and modify the condition to **distance > 20 and distance < 25**. Under this condition, the speaker plays Fa.
6. Duplicate the above code blocks, and modify the condition to **distance > 25 and distance < 30**. Under this condition, the speaker plays So.
7. Duplicate the above code blocks, and modify the condition to **distance > 30 and distance < 35** . Under this condition, the speaker plays La.
8. Duplicate the above code blocks, and modify the condition to **distance > 35 and distance < 40**. Under this condition, the speaker plays Si.
9. At last, add a ![j19](./media/j19.png) to stop the tone playing.

**Complete Test Code**

![6-23-2-2](./media/6-23-2-2.png)

##### 7.23.2.3 Test Result

After uploading code, put your hand in front of the ultrasonic sensor and the speaker will emit sound. You can control the tone by moving your hand in front of the sensor.

Tones corresponding to distance: 

Do: 5-10cm

Re: 10-15cm

Mi: 15-20cm

Fa: 20-25cm

So: 25-30cm

La: 30-35cm

Si: 35-40cm



### 7.24 Button Control Fan

#### 7.24.1 Overview

In this experiment, we program to control the fan by a button.

#### 7.24.2 Test Code

##### 7.24.2.1 Code Flow

![6-24-2-1](./media/6-24-2-1.png)

##### 7.24.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. Declare a variable and name to *item*, and assign the analog value read by ADKey to it.

![](./media/6-24-2-2-1.png)

3. Add a ![j25](./media/j25.png) to determine the value of *item*. When item > 3500 (the red button is pressed), the fan stops. When item > 2000 & item < 3000 (the yellow button is pressed), the fan rotates.
3. At last, add a delay of 0.3s.

![6-24](./media/6-24-2-2-2.png)

**Complete Test Code**

![6-24](./media/6-24-2-2-3.png)



##### 7.24.2.3 Test Result

After uploading code, when we press the yellow button, the fan will turn on. When we press the red button, the fan stops working. 



### 7.25 Auto-door

#### 7.25.1 Overview

Many shopping malls open their doors when someone approaches and close them when no one is detected. Herein, we adopt a PIR motion sensor to simulate this kind of auto-door. The door opens when someone is detected and closes when no one is present.

#### 7.25.2 Test Code

##### 7.25.2.1 Code Flow

![6-25-2-1](./media/6-25-2-1.png)

##### 7.25.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)



2. Drag ![j16](./media/j16.png) to determine the output of PIR motion sensor. If a motion is detected, it will output 1. Otherwise, it outputs 0.

3. When someone is sensed, the servo rotates to 180 degree to open the door. If nothing is detected, the it rotates to 0 degree to close the door.

![6-1-4-1-1](./media/6-1-4-1-1.png)

**Complete Test Code**

![6-25](./media/6-25-2-2.png)

##### 7.25.2.3 Test Result

After uploading code, wave your hand over the PIR motion sensor, and the servo will rotate to 180 degree (door open). After a while, it will back to 0 degree (door close) if nothing is detected.



### 7.26 Access Card

#### 7.26.1 Overview

A common access card is a  magnetic card or a key chain. So in this experiment, we make a simple access device through servo, a magnetic card and an RFID module.

#### 7.26.2 Code Blocks

![](./media/j62.png) 

This block assigns strings. You only need to input strings into it. 

#### 7.26.2 Test Code

##### 7.26.2.1 Code Flow

<p style="color:red;">ATTENTION: '93e64720' is my IC card code in the experiment. You need to replace it with yours (details please see in chapter 7.8).</p>

![6-26-2-1](./media/6-26-2-1.png)

##### 7.26.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Add a ![j27](./media/j27.png) to initialize the RFID module.
3. Declare a string variable named “idCard”

![6-26](./media/6-26-2-2-1.png)

4. In ![](./media/text.png),  drag ![](./media/j62.png) and input “93e64720” ('93e64720' is my IC card code in the experiment. You need to replace it with yours), and put this block into the assignment box of ![6-26](./media/6-26-2-2-1.png)

![6-26](./media/6-26-2-2-2.png)

5. use ![j16](./media/j16.png) to determine the read code of RFID module. If the code is “93e64720”, the servo will rotate to 180 degree and stays for a delay of 3000. If not, the servo will stay still.

![6-26](./media/6-26-2-2-3.png)

**Complete Test Code**

![6-26](./media/6-26-2-2-4.png)

##### 7.26.2.3 Test Result

After uploading code, put your IC card at the sensing area of the RFID module, and the servo will rotate to 180 degree for 3s and then come back. If the card code is not correct, the servo will stay still.



### 7.27 Auto-fan

#### 7.27.1 Overview

The weather is getting hotter in summer, so some public places will be equipped with some auto-fans that sense the ambient temperature value. When the temperature reaches a set value, he fan turns on. We add a PIR motion sensor to lower energy consumption. Thus, the fan will turn on only when the temperature reaches the value and someone is sensed nearby. 

Now let's do it!

#### 7.27.2 Test Code

##### 7.27.2.1 Code Flow

![6-27-2-1](./media/6-27-2-1.png)

##### 7.27.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Declare a variable named “temp”
3. Assign the temperature value read by the sensor to the variable *temp*

![6-27](./media/6-27-2-2-1.png)

4. Add a ![j16](./media/j16.png) to determine whether the temperature value exceeds the set threshold. Add the code that turns off the fan in "else".
5. Add another ![j16](./media/j16.png) to determine the PIR motion sensor value. If it is 1, the fan rotates. Or else, fan stops.

![6-27](./media/6-27-2-2-2.png)

**Complete Test Code**

![6-27](./media/6-27-2-2-3.png)

##### 7.27.2.3  Test Result

After uploading code, when the temperature value is higher than 28 and the PIR motion sensor detects someone, the fan turns on. If one of the two conditions are not satisfied, the fan will not rotate.



### 7.28 Environment Monitoring

#### 7.28.1 Overview

In this project, we use an OLED display to reveal the values of temperature, humidity, air pressure and altitude in the environment. It can be regarded as a mini environmental monitoring device. 

#### 7.28.2 Test Code

##### 7.28.2.1 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Add a BMP388 and OLED initialization block; Add a string block to set its parameters.

![QQ_1721803712158](./media/6-28-2-1-1.png)

3. Read BMP388 module value, and display “Data Sugges” in the center of the first line of OLED. Centered: set cursor to x=30 (the starting cursors vary with strings).

![QQ_1721804274756](./media/6-28-2-1-2.png)

4. Set the starting position of displayed values (Y from 10: the height of the first line).

   Add 3 OLED display blocks and set the display of the first two to "no-warp", set the first line of code to display "T:" (indicating temperature)

   The second line shows the temperature value. The third line shows "C" (temperature in degrees Celsius) and print in "warp" mode.

   ![QQ_1721804842582](./media/6-28-2-1-3.png).

5. Duplicate ![QQ_1721805190266](./media/6-28-2-1-4.png) and modify the content in the first line into “RH:(humidity value)”; The second line will show the humidity value. The third line shows the unit of the value “%”.

   ![QQ_1721805400589](./media/6-28-2-1-5.png)

6. Duplicate ![QQ_1721805428061](./media/6-28-2-1-6.png) and modify the content in the first line into “P:(pressure)”, The second line will show the value. The third line shows the unit of the value “hPa”.

   ![QQ_1721805463843](./media/6-28-2-1-7.png)

7. Duplicate ![QQ_1721805619055](./media/6-28-2-1-8.png) and modify the content in the first line into “ASL:(altitude value)”, The second line will show the value. The third line shows the unit of the value “M”(meter). 

   Add a OLED refresh block and add a delay of 1s. 

   

   ![QQ_1721805906991](./media/6-28-2-1-9.png)

   **Complete Test Code**

   ![6-28-2-2](./media/6-28-2-2.png)

   
   
   

##### 7.28.2.2 Test Result

After uploading code, you will see the values of temperature, humidity, air pressure and altitude on the OLED display.

![6-28-2-2-1](./media/6-28-2-2-1.png)



### 7.29 Car Backing Radar

#### 7.29.1 Overview

When a car is in reverse, it will alarm the distance of the obstacles behind the parking space. In this project, we build a mini car backing radar with an ultrasonic sensor for distance detection, a speaker to alarm, and a traffic light module as an indicator.

#### 7.29.2 Test Code

##### 7.29.2.1 Code Flow

![6-29-2-1](./media/6-29-2-1.png)

##### 7.29.2.2 Build Code

1. Build the two basic blocks:

![6-1-4-1-1](./media/6-1-4-1-1.png)

2. Declare a variable named *distance*

3. Assign the detected value of the ultrasonic sensor to *distance*

	![QQ_1721810318114](./media/6-23-2-2-1.png)

4. Add a ![j25](./media/j25.png) to determine the *distance*. If *distance* > 40, code blocks in it will be executed: the speaker stays quiet, the red LED is off while the green one is ON.

	![QQ_1721868975906](./media/6-29-2-2-1.png)

5. Add another ![j25](./media/j25.png). If *distance* < 40, code blocks in it will be executed: the speaker alarms, the red LED is ON while the green one is off.

	![QQ_1721870782466](./media/6-29-2-2-2.png)

**Complete Test Code**

![6-29-2-2-3](./media/6-29-2-2-3.png)

##### 7.29.2.3 Test Result

After uploading code, when the the detected distance value is greater than 40cm, the green LED is on and the amplifier does not emit sound. If the value is less than 40cm, the red LED will light up and the amplifier will alarm.



### 7.30 RGB Ring Clock

#### 7.30.1 Overview

In this project, we build an informal clock with an RGB ring, whose three colors represent hour, minute and second respectively. Since the ring only boasts 12 beads, each bead is 5 seconds/minutes (60/12=5).

#### 7.30.2 Test Code

##### 7.30.2.1 Code Flow

As shown in the flowchart, we use red for hour, green for minutes, blue for seconds. When second = 60, minute adds 1, and when minute = 60, hour adds 1. 

Note that here we adopt 60/5=12 rather than 59/5=11.8, this is because the variable type is integer and the value should be divided by 5. And 60 can be perfectly divided into 12 parts.

![6-30-2-1](./media/6-30-2-1.png)

##### 7.30.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)

2. Initialize the serial port and set baud rate to 9600. 

	Initialize RGB module and declare three variables named *hour*, *minute*, *second* respectively. We assign them initial values, for example, we set the time to 10: 30: 40

![QQ_1721895321044](./media/6-30-2-2-1.png)

3. In ![QQ_1721895350840](./media/myBlocks.png), we build a function block. Click ![QQ_1721895399311](./media/6-30-2-2-2.png) to name the function. Here we name it *clockCode*, click ok.

   ![QQ_1721895561889](./media/6-30-2-2-3.png)

4. Function block: ![QQ_1721895613952](./media/6-30-2-2-4.png). Add code blocks under this block to define the function. This block is placed separately, when using, drag ![QQ_1721895716867](./media/6-30-2-2-5.png) in ![QQ_1721895350840](./media/myBlocks.png) and put it at the position as needed. 

5. Add a ![QQ_1721895820024](./media/6-30-2-2-6.png) to count seconds. Then add a ![j25](./media/j25.png) to determine whether second value is greater than 59. If yes, minute+1 and zero out second.

![QQ_1721896005372](./media/6-30-2-2-7.png)

6. Add another ![j25](./media/j25.png) to determine whether minute > 59. If yes, hour+1 and zero out minute. 

	Drag one more ![j25](./media/j25.png) and put it in the above ![j25](./media/j25.png) to determine whether hour > 12. If yes, hour = 1.

![](./media/6-30-2-2-8.png)

7. Add a delay of 1s, and print the values of hour, minute, second on serial monitor. 

![QQ_1721896392541](./media/6-30-2-2-9.png)

8. Call the function clockCode. In ![QQ_1721895350840](./media/myBlocks.png), drag ![QQ_1721895716867](./media/6-30-2-2-5.png) and place it into ![j2](./media/j2.png). 

	Till now, these are all code blocks of time counting and display. Parts below are settings of beads to light on according to time. 

9. Add ![j16](./media/j16.png) to determine whether second is 0 after dividing by 5. If second=0, current time is within 5s. So we light up the 12th beads of the RGB ring. Pay attention that add a ![j51](./media/j51.png) above. If it is not 0, light up the bead at **(second / 5) - 1**. For instance, when second=30, and 30/5-1=5, so 5th bead lights up. (We set the variable type to integer (int), so the division remainders are omitted.) Second is in BLUE.

![QQ_1721897532506](./media/6-30-2-2-10.png)

10. Similarly, set the minute. The difference is that this part is without a clear block. Minute is in GREEN.

![QQ_1721897597770](./media/6-30-2-2-11.png)

11. When setting hours, only **hour-1** without being divided by 5. Hour range 1-12h corresponds to beads 0-11. Hour is in RED. At last, add a ![j52](./media/j52.png).

**Complete Test Code**

![6-30-2-2](./media/6-30-2-2.png)

##### 7.30.2.3 Test Result

Before uploading code, you need to input an initial time in the following blocks of variables hour, minute, second. Herein, we set to 10: 30: 40.

![QQ_1721897911774](./media/6-30-2-3.png)

After uploading code, you will see the RGB ring shows the time: red for hour, green for minute, blue for second. A minute passes as blue runs a circle. 

Only one color will be displayed when they are overlapped. Blue will not cover green while green will not cover red. 

<p style="color:red;">Note that this is an informal clock without a clock chip. So its errors begin to accumulate over time.</p>



### 7.31 Joystick Control Servo

#### 7.31.1 Overview

We control the servo via the axis X of the joystick. This model is widely applied to mechanical ON/OFF of lights and doors.

#### 7.31.2 Test Code

##### 7.31.2.1 Code Flow

![6-31-3-1](./media/6-31-3-1.png)

##### 7.31.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Declare a variable *angle* and assign the x value of joystick to *angle*.

![QQ_1722042398784](./media/6-31-3-2-1.png)

3. Add a ![j25](./media/j25.png) to determine whether *angle* > 3500. If yes, servo rotates to 0 degree.

![QQ_1722042751659](./media/6-31-3-2-2.png)

4. Add a ![j25](./media/j25.png) to determine whether *angle* < 500. If yes, servo rotates to 180 degree.

![image-20240727091322352](./media/6-31-3-2-3.png)

**Complete Test Code**

![QQ_1722040933018](./media/6-31-3-2-4.png)

##### 7.31.2.3 Test Result

After uploading code, push the joystick to the left and the servo rotates to 180 degree. Push it to the right and the servo rotates to 0 degree.



### 7.32 Ultrasonic Ranger

#### 7.32.1 Overview

In this project, we combine the ultrasonic sensor and the OLED module to build a distance meter, whose detection range is 4-300CM.

#### 7.32.2 Test Code

##### 7.32.2.1 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Initialize OLED module by ![j53](./media/j53.png)
3. Add a ![j54](./media/j54.png) and set text size to 12x16
4. Declare a variable *distance* and assign the value detected by the ultrasonic sensor to *distance*

![QQ_1722046131988](./media/6-32-2-1-1.png)

5. Add a ![j58](./media/j58.png) to clear the logo displayed on OLED

6. Add an OLED module to display “Distance:” on the first line and show the value of *distance* on the second line. Add the unit of “CM” after the value. 

6. At last, add a refresh block.

   ![QQ_1722046707083](./media/6-32-2-1-2.png)

**Complete Test Code**

![6-32-1-2](./media/6-32-1-2.png)

##### 7.32.2.2 Test Result

After uploading code, “Distance:” will be displayed on the first line. What followed is the distance value in “CM” in the second line.

![6-32-2-2](./media/6-32-2-2.png)



### 7.33 Compass

#### 7.33.1 Overview

The AK8975 module is adopted to read direction values. According to these values, the OLED displays different arrows.

#### 7.33.2 Test Code

##### 7.33.2.1 Code Flow

![6-33-2-1](./media/6-33-2-1.png)

##### 7.33.2.2 Build Code

1. Build the two basic blocks:![6-1-4-1-1](./media/6-1-4-1-1.png)
2. Initialize AK8975 module and OLED display, declare a variable “direction”.

![](./media/6-33-2-2-1.png)

3. Clear the OLED, and assign the direction value of AK8975 to the variable *direction*

![](./media/6-33-2-2-2.png)

4. Add a ![j25](./media/j25.png) to determine whether 340 < direction < 360. If yes, OLED shows “↑”.

	Block condition: direction > 340 and direction < 360

![](./media/6-33-2-2-3.png)

5. Duplicate blocks and determine whether direction > 230 and direction < 250. If yes, OLED shows “→”.
6. If direction > 140 and direction < 170, OLED shows “↓”.
7. If direction > 70 and direction < 90, OLED shows “←”.

![](./media/6-33-2-2-4.png)

8. Add an OLED refresh block and add a delay of 0.5S.

**Complete Test Code**

![6-33-2-2](./media/6-33-2-2.png)

##### 7.33.2.3 Test Result

After uploading code, the arrow on the OLED will nearly point to the South. Move the programming box and you will see the direction changes. 



### 7.34 WiFi

#### 7.34.1 Overview

ESP32 boasts a built-in Wi-Fi and Bluetooth nodule that is widely used in Internet of Things (IoT). With this function, it can remotely control the data transmission through the wireless network. Generally, developers program via an Arduino IDE or ESP-IDF to connect the ESP32 to the Internet via a WiFi connection to a router.

In applications, ESP32 can be used as a client to connect to a Wi-Fi network, or as a hotspot to create its own network. Through these connections, ESP32 receives commands to control external devices, such as turning on/off lights and adjusting temperature. In the code, protocols like HTTP and MQTT are used to communicate with the server to achieve data sending and receiving, so as to remotely control and monitoring.

#### 7.34.2 Code Blocks

1. ![](./media/j63.png) 

	This block initialize wifi module. You need to set the name and passwords of your wifi.

2. ![QQ_1722058950827](./media/j64.png) 

	This block reads the IP address after esp32 connecting to wifi, and print it on serial monitor.

3. ![](./media/j65.png) 

	This block updates the sensor values in real time. Input the value name in the first box and its unit in the second one. 

	After that, choose a card ID, which should varies with modules. The value to be displayed is in the final box. 

4. ![QQ_1722222062997](./media/j66.png) 

	This block adds the web buttons. Set the button usage in the card label. For example, red LED. This is in order to separate buttons. 

	The card ID cannot be the same in the code.

#### 7.34.3 ESP32 WiFi Introduction

ESP32 development board comes with built-in Wi-Fi (2.4G) and Bluetooth (4.2), which enable it to easily connect to Wi-Fi network and communicate with other devices in the network. You can display web pages in your browser via ESP32.

![6-34](./media/6-34-3-1.png)

- Base station mode (STA / Wi-Fi Client mode): ESP32 is connected to Wi-Fi hotspot (AP).
- AP mode (Soft-AP / Wi-Fi hotspot mode): Wi-Fi device(s) is(are) connected to ESP32.
- AP-STA mode: ESP32 is both Wi-Fi hotspot and a Wi-Fi device connected to another Wi-Fi.
- These modes supports multiple security modes, including WPA, WPA2 and WEP.
- It is able to scan Wi-Fi hotspot (active or passive)
- It support promiscuous mode monitoring IEEE802.11 Wi-Fi packets.

------

For more wifi reference, please visit https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html

espressif official: https://www.espressif.com.cn/en/home

![6-34](./media/6-34-3-2.png)

####  7.34.4 Test Code

**Add wifi web page library first:**

- Click ![st130](./media/6-34-4-1.png) to add an Extension

- Click communication to load “**Web Page Editing PRO**”.

![6-34](./media/6-34-4-2.png)

1. In ![](./media/wifi.png), set the name and passwords of your wifi in block ![](./media/j63.png).

2. Display the IP address of the wifi on the OLED

![QQ_1722069311103](./media/6-34-4-3.png)

3. Set up a web element named *temperature* in the unit of ℃.

Code block:

![st136](./media/6-34-4-4.png)

Web page:

![st136-1](./media/6-34-4-5.png)

4. Add a button, set the type to button

Code block:

![st141](./media/6-34-4-6.png)

Web page:

![st141-1](./media/6-34-4-7.png)

**Complete Test Code**

![6-34-3](./media/6-34-4.png)

#### 7.34.5 Test Result

After uploading code, the OLED will display the IP address. Connect your computer/mobile phone and ESP32 to the same wifi, and you can access the IP address to see the control page through your device.

PC:

![st132](./media/6-34-5-1.png)

Mobile:

![st133](./media/6-34-5-2.png)



### 7.35 WiFi Real-time Display

#### 7.35.1 Overview

In this project, we display the values of temperature and humidity sensor, pressure sensor, photoresistor, sound sensor, PIR motion sensor and ultrasonic sensor on the web page. 

#### 7.35.2 Test Code

##### 7.35.2.1  Build Code

1. Initialize BMP388 and wifi, set the name and passwords of wifi.

	Initialize OLED and display the IP address of the wifi on it.

![](./media/6-35-2-2.png)

2. set values on web page through block ![](./media/j65.png)

   

![6-35-2-1](./media/6-35-2-1.png)

##### 7.35.2.2 Test Result

Upload the code, and the OLED shows the IP address after connecting to wifi. 

Connect your computer/mobile phone and ESP32 to the same wifi, and you can access the IP address to see the values through your device. 

If you are using a mobile phone hotspot, you can directly access the IP via the phone.

![](./media/6-35-2-3.png)



### 7.36 WiFi Control

#### 7.36.1 Overview

We control LED, servo and the fan on the web page button wirelessly. 

#### 7.36.2 Test Code

##### 7.36.2.1 Build Code

1. Initialize wifi and OLED, display the IP address of the wifi on the OLED. Name a variable used to switch sensor state according to the corresponding functions, for example, we name redLed to represent the red led.

![QQ_1722234105165](./media/6-36-2-1-1.png)

2. Set web buttons and add functions of buttons by block ![QQ_1722222062997](./media/j66.png); Add ![j16](./media/j16.png) to determine whether the value = 0. If yes, execute code in “then”. If not, run code in “else”. 

	We take red led as an example. Initially, redLed = 0. When the red led button is pressed, the red led will light up and redLed becomes 1. When you press this button next time, code in “else” will be execute, so the led goes off and redLed = 0 again. 

![QQ_1722234332241](./media/6-36-2-1-2.png)

3. Similarly, set blocks of yellow led, green led, Servo and motor.

**Complete Test Code**

![6-36-2-1](./media/6-36-2-1.png)

#####    7.36.2.2 Test Result

Upload the code, and the OLED shows the IP address after connecting to wifi. 

Connect your computer/mobile phone and ESP32 to the same wifi, and you can access the IP address to see the control page through your device. 

![](./media/6-36-2-2.png)



### 7.37 WiFi Piano

#### 7.37.1 Overview

In this project, we set seven buttons to control the speaker to play tones of Do, Re, Mi, Fa, So, La, Si.

#### 7.37.2 Test Code

##### 7.37.2.1 Build Code

1. Initialize wifi and OLED module, display the IP address of the wifi on the OLED
2. define buttons through ![QQ_1722222062997](./media/j66.png), modify the button names and functions, press buttons to play tones of Do, Re, Mi, Fa, So, La, Si.

**Complete Test Code**

![6-37-2-1](./media/6-37-2-1.png)

##### 7.37.2.2 Test Result

Upload the code, and the OLED shows the IP address after connecting to wifi. 

Connect your computer/mobile phone and ESP32 to the same wifi, and you can access the IP address to see the control page through your device. 

![](./media/6-37-2-2.png)



### 7.38 Smart Control Panel

#### 7.38.1 Overview

Combined web buttons and wireless control, this control panel in this project is able to control modules and read module values as well. 

#### 7.38.2 Test Code

##### 7.38.2.1 Build Code

1. Initialize wifi and OLED module, set the name and passwords of the wifi

2. Set the values to be displayed through block ![](./media/j65.png)

3. Define button names and functions through block![QQ_1722222062997](./media/j66.png)


**Complete Test Code**

![6-38-2-1](./media/6-38-2-1.png)

##### 7.38.2.2 Test Result

Upload the code, and the OLED shows the IP address after connecting to wifi. 

Connect your computer/mobile phone and ESP32 to the same wifi, and you can access the IP address to see the control page through your device. 

![QQ_1722241479429](./media/6-38-2-2.png)
