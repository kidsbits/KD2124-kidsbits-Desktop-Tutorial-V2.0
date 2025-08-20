# 2.1 KidsBlock Desktop Graphical Programming

KidsBlock Desktop is a graphical programming tool designed to help children and beginners learn programming. It uses a visual programming interface to build programs by dragging code blocks rather than writing codes directly. This is especially suitable for users without programming background, as it simplifies the process and lowers the learning threshold.

**Main Features:**

1. **Graphical interface**: Users create programs by dragging code blocks with different functions (such as loops, conditional judgments, variables, etc.), rather than learning complex code syntax issues. 
2. **Educational orientation**: It is designed for children and teens with a user-friendly interface, and it helps them learn programming thinking and logic in fun.
3. **Interactive learning**: Through graphical programming, children see how the programs they write process and respond in real time, increasing the joy and interactivity.
4. **Diversified functional blocks**: It provides a wealth of blocks for the creation of different types of programs and projects, including simple animations, games and gadgets.
5. **Easy to expand**: Some versions of KidsBlock are able to extend the functionality through custom modules or plug-ins, thus providing more programming possibilities.

With graphical programming, KidsBlock Desktop aims to stimulate children's interest in programming and develop their problem-solving and logical thinking skills.

# 2.2 Install Kidsblock on Windows

1.Download Kidsblock package: [http://xiazai.keyesrobot.cn/KidsBlock.exe](http://xiazai.keyesrobot.cn/KidsBlock.exe)

2.Click “KidsBlock Desktop.exe”.

![k1](./media/k1.png)

3.Tick “**Anyone who uses this computer(all users)**” and click “**Next**”.

![img](./media/k2.jpg)

4.Click “**Browse...**” to choose a path for the software (here we choose Disk C) and then “**Install**”.

![k3](./media/k3.png)

![k4](./media/k4.png)

5.Click “Finish” and open Kidsblock.

![5](./media/k5.png)

6.If a warning interface pops up, just “**Allow access**”. 

​	Main interface of Kidsblock:

![6](./media/k6.png)



# 2.3 Install Kidsblock on MacOS

1.Download Kidsblock package: [https://xiazai.keyesrobot.cn/KidsBlock.dmg](https://xiazai.keyesrobot.cn/KidsBlock.dmg)

![k7](./media/k7.png)

2.After downloading, Click KidsBlock. Drag the icon of KidsBlock Desktop into Applications.

![8](./media/k8.png)

3.After installation, you can see the icon of KidsBlock.

![k9](./media/k9.png)



# 2.4 Kidsblock

(**Here we demonstrate on Windows, and it can be a reference for MacOS.**)

## 2.4.1 Main Interface Functions 1

![k10](./media/k10.png)

## 2.4.2 Languages

Click ![img](./media/k11.jpg) to choose “English” or “简体中文”: ![image-k12](./media/k12.png)

## 2.4.3 Driver

**NOTE: If the driver has already installed on your computer, please skip the following steps.**

Click ![img](./media/k13.jpg) to choose “**Install driver**”.

![k14](./media/k14.png)

A. Welcome to the Device Driver Installation Wizard and click “**Next**”.

![k15](./media/k15.png)

B. “**Finish**”.

![k16](./media/k16.png)

C. “**Next**”

![k17](./media/k17.png)

D. “**Finish**”

![k18](./media/k18.png)

E. If a warning interface pops up, just “**Allow**”. And then click “**Install**”.

![k19](./media/k19.png)

F.“**Install**”

G. “**Finish**”

![k20](./media/k20.png)

H. “**Extract**”

![k21](./media/k21.png)

I. “**Next**”

![k22](./media/k22.png)

J. Tick “**I accept this agreement**” and then “**Next**”.

![k23](./media/k23.png)

K. “**Finish**”

![k24](./media/k24.png)

L. “**INSTALL**”

![k25](./media/k25.png)

M. Wait for the completion of driver installing. And click “**OK**”.

![k26](./media/k26.png)

## 2.4.4 Development Board

Click ![img](./media/k27.jpg) to choose a control board. We have integrated the board we need in this software: click “Kit” and find “ESP32 coding box” to “**Connect**”. After connecting, “**Go to Editor**”. 

![](./media/k31.png)

![](./media/k32.png)

![](./media/k33.png)

![img](./media/k27.jpg) changes into ![](./media/k29.png), and ![img](./media/k28.jpg) changes into ![](./media/k30.png). These means ESP32 board and COM port are both connected.

![](./media/k34.png)

## 2.4.5 Serial Port

If the ESP32 board is connected but ![img](./media/k28.jpg) does not change into ![](./media/k30.png), we need to set a COM port manually. 

Click ![img](./media/k28.jpg) and “**Connect**”. When you see "connected", the port is set.

![](./media/k36.png)

![](./media/k32.png)

![](./media/k33.png)

Disconnection: click ![](./media/k30.png) and “**Disconnect**”.

![](./media/k34.png)

![](./media/k41.png)

## 2.4.6 Main Interface Functions 

![](./media/k42.jpg)

## 2.4.7 Extensions

**NOTE: All required modules are integrated in main board, so this section is for reference.**

Extensions: ![img](./media/k43.jpg)

Click ![img](./media/k43.jpg) to search and load sensors/modules. For instance, click “passive buzzer” ![img](./media/k44.jpg) and “**Not loaded**” changes into “**Loaded**”. Passive buzzer is added.

![img](./media/k45.jpg)![img](./media/k46.png)   ![img](./media/k47.jpg)

Click ![img](./media/k48.jpg) to back to editor, and you will see the Passive buzzer block.

![img](./media/k49.jpg)

If you want to remove it, enter ![img](./media/k43.jpg) and click ![img](./media/k44.jpg) again, and “Loaded” changes into “Not loaded”. That means this block is removed. 

![img](./media/k47.jpg)![img](./media/k46.png)   ![img](./media/k45.jpg) 

## 2.4.8 How to open code

**Method 1:**

Click the SB3 file you want to load. If you want to open ![](./media/k50.png), click it to directly load to the software. After that, connect to the board and port.

![](./media/k54.png)

**Method 2:**

Open Kidsblock and click “**file**” to choose “**Load from your computer**”, open a file of .SB3, for example, ![](./media/k50.png).

![](./media/k52.png)

![](./media/k53.png)

![](./media/k54.png)



## 2.4.9 Upload Code and Set Baud Rate

### 2.4.9.1  Upload Code

Load ![](./media/k50.png) into Kidsblock, and set the development board and port. Click ![image-20230425155752592](./media/k55.png).

![](./media/k56.png)

![](./media/k57.png)

After uploading, the printing box of Kidsblock prints “Hello KidsBlock”.

![](./media/k58.png)

### 2.4.9.2 Set Baud Rate

Set printing box: ![](./media/k59.png)

![](./media/k60.png): small

![](./media/k61.png): large

![](./media/k63.png): none

If there is no output or it outputs garbled words, please click ![](./media/k62.png) to set baud rate first. The baud rate should be consistent with the code. Here it is 9600.

![](./media/k64.png)

