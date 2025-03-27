![[5.pdf]]



라즈베리파이 특징
- 라즈베리파이는 작은 single board computer 이다.
- 라즈베리파이 구성요서
1. USB port
2. SD card slot
3. Audio jack
4. Ethernet port
5. HDMI port
6. Micro USB power connector
7. GPIO ports

__Things that you should never do__
1. Do not shut the RPi down by pulling out the USB power supply
2. Do not place a powered RPi on metal surfaces. **short circuit**
3. GPIO pins are 3.3V tolerant. Do not connect a circuit that is powered at 5V
4. Do not connect circuits that aplly power to the GPIO header while the RPi is not powered on. reverse **current flow.**

 Raspberry Pi Software
1. The main open source Linux distribution used on RPi board include Raspbian, Ubuntu, and Arch Linux
2. Raspbian is a version of Debain that is released specifically for the RPi
3. __Raspbian__ extends Debian with RPi-specific tools and software packages

Interfacing with the Raspberry Pi
- Remote Access via __Secure Shell(SSH)__
1. SSH is a network __protocol__ for secure encrypted communication between network devices
2. Use an SSH terminal client to connect to SSH server running on port22 of PRi
3. Only have access to command line not full desktop environment
4. For a full remote desktop, use __Virtual Network Computin (VNC)__
	->VNC is a graphical desktop sharing system that allows you to remotely control the desktop interface of one computer from another computer or mobile device

Remote Access via Secure Shell(SSH)
- Enable SSh
1. Lanunch Raspberry Pi Configuration from the Pereferences menu
2. Naviagte to the Interfaces tab
3. Select Enabled next to SSH
4. Click OK
- Set up client
1. SSH using Windows 10/11
2. To connect to yout Pi from a different computer, copy and paste the following command into the terminal window

__$ssh pi@<IP 주소>__

라즈베리파이 기본 이름 :  __pi__
비밀번호                         : raspberry
ex) ssh ikram@192.168.1.5

Interfacing with the Raspberry Pi
- Secure Shell Connections Using PuTTY
1. PuTTY is a free, open source terminal emulator, serial console, and SSH client that you can also use to connect to the PRi over the network
2. It supports serial and SSH connections
3. It installs an application called psftp that enables you to transfer files to and from the PRi over the network from your desktop computer


[[리눅스 명령어]]

[[C compile]]

