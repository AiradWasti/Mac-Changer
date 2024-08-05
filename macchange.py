#!/usr/bin/python

import subprocess
import re
import os
import sys
from termcolor import colored

def validate_mac(mac):
    """Validate MAC address format."""
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        return True
    return False

def validate_interface(interface):
    """Check if the network interface exists."""
    try:
        subprocess.check_output(["ip", "link", "show", interface])
        return True
    except subprocess.CalledProcessError:
        return False

def change_mac_address(interface, mac):
    """Change the MAC address of the specified interface."""
    try:
        subprocess.check_call(["sudo", "ip", "link", "set", interface, "down"])
        subprocess.check_call(["sudo", "ip", "link", "set", interface, "address", mac])
        subprocess.check_call(["sudo", "ip", "link", "set", interface, "up"])
    except subprocess.CalledProcessError as e:
        print(colored(f"Failed to change MAC Address: {e}", "red"))
        sys.exit(1)

def main():
    if os.geteuid() != 0:
        print(colored("This script must be run as root. Use 'sudo'.", "red"))
        sys.exit(1)

    interface = input(colored("Enter Interface To Change MAC Address On: ", "blue")).strip()
    new_mac_address = input(colored("Enter MAC Address to Change To: ", "blue")).strip()

    if not validate_interface(interface):
        print(colored(f"Interface {interface} does not exist.", "red"))
        sys.exit(1)

    if not validate_mac(new_mac_address):
        print(colored("Invalid MAC Address format.", "red"))
        sys.exit(1)

    before_change = subprocess.check_output(["ip", "link", "show", interface])
    change_mac_address(interface, new_mac_address)
    after_change = subprocess.check_output(["ip", "link", "show", interface])

    if before_change == after_change:
        print(colored(f"Failed to change MAC Address to {new_mac_address}.", "red"))
    else:
        print(colored(f"MAC Address changed to {new_mac_address} on interface {interface}.", "green"))

if __name__ == "__main__":
    main()
