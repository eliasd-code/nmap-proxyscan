# nmap-proxyscan
# A script that lets you scan anonymously on the internet

# by eliasd
https://github.com/eliasd-code

Description:
With the nmap-proxy you can anonymously scan ports, services etc.
Using is very easy, provided you have already worked with nmap and Linux.
It scans for the ports you give it and stores its output in the .log file.
You need three packages to use it
once the gate packet:
$ sudo apt install tor
$ sudo pacman -S tor

then you need python3:
$ sudo apt install python3
$ sudo pacman -S python3

and of course proxychains:
$ sudo apt install proxychains
$ sudo pacman -S proxychains

to run the tool simply:
$ sudo su
$ python3 [Filename]
Enter # and follow the instructions.


!!!!CAUTION!!!!
I cannot guarantee that you will remain anonymous! You are responsible for the proxies you use! This tool only uses your pre-configured proxies (/etc/proxychains.conf, it doesn't improve anything!
