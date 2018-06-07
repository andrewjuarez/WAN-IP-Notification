"""
Makes a JSON request to an external server for the WAN IP address of host.
Saves the WAN IP address to a text file 'WAN_IP.txt' by default.

Author: A. Juarez
Date: 5/16/18
"""
import urllib.request;
import time;

TARGET_FILE = "WAN_IP.txt"

def get_ip():
    """ JSON request to get public IP address """
    src = urllib.request.urlopen("https://api.ipify.org/?format=json")
    getsrc = src.read()
    ip = getsrc.decode('ASCII')
    ip.strip()
    return ip


def save_ip(ip):
    """ Write the new IP address to file """
    file = open(TARGET_FILE, "w")
    file.write("Updated: " + time.asctime(time.localtime(time.time())))
    file.write("\n")
    file.write(ip)    
    file.close()

def check_ip(ip):
    """ Returns True if the IP is out of date."""
    try:
        file = open(TARGET_FILE, "r")
        existing_ip = file.readlines()[1]
        file.close()
    except FileNotFoundError:
        return True
    
    if (existing_ip.strip() != ip.strip()):
        return True
    else:
        return False

if __name__ == "__main__":
    ip = get_ip()
    if(check_ip(ip)):
        print("The ip is out date!")
        save_ip(ip)
    else:
        print("The ip is up to date!")
