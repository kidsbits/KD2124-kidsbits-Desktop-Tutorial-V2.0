MicroPython is a stripped-down version of Python 3 language, which includes a small portion of the Python standard library. It can run in microcontrollers and restricted environments after being optimized. Here are the main features of MicroPython:

1. **Compatibility**: MicroPython strives to be as compatible as possible with normal Python (CPython), which means that if you know Python, you already know the basics of MicroPython. 
2. **Hardware access**: In addition to core Python libraries, MicroPython includes modules such as "machines" for accessing low-level hardware, giving developers direct control over the hardware resources of the microcontroller. 
3. **Interactive prompt (REPL)**: MicroPython provides an interactive prompt (REPL) so that users execute commands directly from a desktop computer on an embedded platform. This is very useful for fast real-time testing and debugging of embedded systems. 
4. **Multi-threading support**: MicroPython firmware supports multi-threading, which enables a single microcontroller to handle multiple embedded tasks simultaneously, thus speeding up the executions.
5. **Open source project**: MicroPython is an open source project whose source code is available on Github. It follows the MIT license and is free to use for educational and commercial purposes. 
6. **Wide support**: MicroPython supports a variety of microcontroller boards and RTOS (real-time operating systems), such as ESP32, ESP8266, STM32, etc. In addition, it also provides rich libraries and modules to meet different development needs. 

# 2.1 Download Thonny

## 2.1.1 Windows

**OS: Windows 10**

Download: [Thonny Official](https://thonny.org)

Move your mouse to “Windows” and you will see the optional versions.

![1101](./media/6-1-1.png)

![1102](./media/6-1-2-2.png)

## 2.1.2 MAC

Similar to Windows.

![1103](./media/6-1-3.png)

![1104](./media/6-1-4.png)

# 2.2 Install Thonny

Two methods:

- Install Thonny+Python package

	Recommended for beginners: When you install, the Python environment and Thonny will be packaged so both installed. There are also two ways to install the package:

	- Installer

		![1201](./media/6-1-5.png)

	- Portable variant

		![1202](./media/6-1-6.png)

- Install Thonny only

  Recommended for developers: When the user already has a python environment, `pip install thonny` comes in handy to install Thonny separately.

  ![1203](./media/6-1-7.png)

Please just install according to your needs.

## 2.2.1 Installer

Here we demonstrate how to install `Installer with 64-bit Python 3.10` on <span style="background:#ff0;color:#000">64bit Windows 10</span>.

(1）After downloading, click ![1204](./media/6-1-8.png) . And you will see **Select Setup Install Mode**, choose **Install for me only**.

![1205](./media/6-1-9.png)

（2）**Next** .

![1206](./media/6-1-10.png)

（3）Tick **I accept the agreement** and **Next**.

![1207](./media/6-1-11.png)

（4）The default path is Disk C, or you can click **Browse...** to modify the path. After that, click **Next**.

![1208](./media/6-1-12.png)

（5）Choose a path to create the program's shortcuts, and click **Next**.

![1209](./media/6-1-13.png)

（6）Tick **Create desktop icon** and click **Next**.

![1210](./media/6-1-14.png)

（7）Install.

![1211](./media/6-1-15.png)

（8）“**Finish**”

![1212](./media/6-1-16.png)

（9）Open Thonny and choose your language.

![1213](./media/6-1-17.png)

（10）Main interface:

![1214](./media/6-1-18.png)

## 2.2.2 Portable Variant

Here we demonstrate how to install `Portable variant with 64-bit Python 3.10` on <span style="background:#ff0;color:#000">64bit Windows 10</span>.

(1）After downloading and being unzipped, click ![1105](./media/6-1-19.png) to choose your language.

![1213](./media/6-1-17.png)

（2）Main interface:

![1214](./media/6-1-18.png)

（3）For convenience, please send it to Desktop(create shortcut).

![1215](./media/6-1-20.png)

Shortcut: ![1216](./media/6-1-21.png)



# 2.3 Board Driver

During installing, please connect the coding box to the computer!

## 2.3.1 Windows：

![](./media/6-3-1.png)

windows 10 and later versions boasts their own drivers. If your computer is, connect the box and click Computer – attribute – Device Manager.

![](./media/6-3-2-2.png)

As follows, if you see a yellow exclamation mark, you need to install manually,

![new(14)](./media/6-3-3.png)

Click ![](./media/6-3-4.png) to Upload driver. 

![](./media/6-3-5.png)

“Brose my computer for drivers”.

![](./media/6-3-6.png)

Find and open the driver file **usb_ch341_3.1.2009.06**.

![](./media/6-3-7.png)

Close the interface and wait for connection.

![](./media/6-3-8.png)

As follows:

![](./media/6-3-2-2.png)

## 2.3.2 MAC：

![](./media/6-3-10.png)

Step 1: Download the driver from the Website and extract the file to the local installation directory.

![](./media/6-3-11.png)

Step 2: For details about how to install the driver in pkg format by default, see Step 3. If OS X 11.0 or later does not support Rosetta, refer to Step 4 to install the dmg driver.

Before installation, please forward to “System Preferences”->“Security & Privacy”->“General” page, below the title “Allow apps downloaded from:” choose the choice 2->“Mac App Store and identified developers”, then the driver will work normally.

![20221232](./media/6-3-12.png)

Step 3: To install the driver in pkg format, tap the driver file → Continue→ Install

![](./media/6-3-13.png)

![20221226083](./media/6-3-14.png)

Then the installation will be successful

![20221226084](./media/6-3-15.png)

![2022122605](./media/6-3-16.png)

To install the pkg format driver on OS X 11.0 and later: Open “LaunchPad”→“CH34xVCPDriver”→Install

![2022122606](./media/6-3-17.png)

When using OS X 10.9 to OS X 10.15, click “Restart” to restart your computer, and perform the following steps after the restart.

![20221226097](./media/6-3-18.png)

Step 4: To install the dmg driver, tap the dmg file and drag “CH34xVCPDriver” to enter the application folder in the operating system.

![2022122608](./media/6-3-19.png)

Then open “LaunchPad”→“CH34xVCPDriver”→Install

![202212269](./media/6-3-20.png)

Then the installation will be successful

![202212260910](./media/6-3-21.png)

When inserting the CH340 control board into the USB port, open System Report -> Hardware ->USB. On the right is USB Device Tree. If the USB device is working properly, you will find a device whose “Vendor ID” is [0x1a86].

![20221226011](./media/6-3-22.png)

Open “Terminal” program under Applications-Utilities folder and type the command “ls /dev/tty*”.

![202212271312](./media/6-3-23.png)

You should see the “tty.wchusbserialx” where “x” is the assigned device number similar to Windows COM port assignment.

# 2.4 Burn FIRMWARE

MicroPython firmware is required to operate on ESP32.

![](./media/6-4-1.png)

A. Connect the coding box to computer after installing driver. USB port cannot be recognized if there is no driver.

B. Click `Run` and `Configure interpreter...`

![6-5-1](./media/6-4-2-2.png)

C. Set interpreter to `MicroPython(ESP32) `, check the port in Device Manager. Click `install or updare MicroPython(esptool)`

![QQ_1722306274285](./media/6-4-3.png)

D. Click ![QQ_1722306727019](./media/6-4-4.png) to choose `Select local MicroPython image...`

![6-5-3](./media/6-4-5.png)

E. Open file `esp32-20210902-v1.17.bin`

![QQ_1722307085225](./media/6-4-6.png)

F. Click `install` and wait. 

![QQ_1722307194334](./media/6-4-7.png)

![QQ_1722307359022](./media/6-4-8.png)

# 2.5 Thonny

## 2.5.1 Interface

Click **View** and tick **Files** to open the file path management.

![1401](./media/6-5-1.png)

![1402](./media/6-5-2-2.png)

## 2.5.2 Toolbar

![1403](./media/6-5-3.png)

|            ICON             |            FUNCTION            |
| :-------------------------: | :----------------------------: |
| ![1404](./media/6-5-4.png)  |          New (Ctrl+N)          |
| ![1405](./media/6-5-5.png)  |        Open... (Ctrl+O)        |
| ![1406](./media/6-5-6.png)  |         Save (Ctrl+S)          |
| ![1407](./media/6-5-7.png)  |    Run current script (F5)     |
| ![1408](./media/6-5-8.png)  |      Debug current script      |
| ![1409](./media/6-5-9.png)  |         Step over (F6)         |
| ![1410](./media/6-5-10.png) |         Step into (F7)         |
| ![1411](./media/6-5-11.png) |            Step out            |
| ![1412](./media/6-5-12.png) |          Resume (F8)           |
| ![1413](./media/6-5-13.png) | Stop/Restart backend (Ctrl+F2) |



# 2.6 Testing ESP32 MicroPython

Download the project file in `1.1 Code Download`

![image-20250724085125977](./media/image-20250724085125977.png)

Click on 'This computer' in the “Files” section and enter the 'Codes' file according to the location where the file is stored

![](./media/6-6-1.png)

Connect to the coding box. If you cannot see the port, please install driver. If the code still cannot be uploaded after connecting to the port, please check whether the firmware is installed to the box. For how to download them, please refer to:

Driver: `2.3 Board Driver`; Firmware: `2.4 Burn FIRMWARE`

![](./media/6-6-2-2.png)

## 2.6.1 Test Shell Command

Input the following code in Shell.

```python
print('hello world')
```

![1501](./media/6-6-3.png)

Press "Enter" and the Shell prints **hello world**.

![1502](./media/6-6-4.png)

## 2.6.2 Test Online Running

Click to open code **3-1-led.py**.

![](./media/6-6-5.png)

Click ![1407](media/6-5-7.png) to run the code, and the LED on the board will flashes: on for 1s and off for 1s.

## 2.6.3 Test Offline Running

Click ![1404](media/6-5-4.png) to create a new script, copy and paste **3-1-led.py** in the editing area.

![](./media/6-6-6.png)

Click ![1406](media/6-5-6.png) to save it to MicroPython device.

![](./media/6-6-7.png)

We name it as **main.py**.

![](./media/6-6-8.png)

After saving, the main.py code will automatically execute as long as the coding box is powered on. You will see the red LED flashes per second. Note that it will not run after saving unless the reset button is pressed.

If you want to run a code offline, it must be loaded to the coding box with a name of `main.py`.











