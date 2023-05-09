#!/bin/python3
import subprocess
import re
import optparse

def changeMac():
    interface=""
    newMac=""
    #parsing interface id and MAC address as parameters
    parser= optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface",help="Interface to change the MAC address")
    parser.add_option("-m","--macAddress", dest="newMac",help="New MAC address")
    (options,arguments) = parser.parse_args()
    interface = options.interface
    newMac = options.newMac
    if not interface:
        interface = str(input("Input the interface name: "))
    #MAC addr filter
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

    #Obtaining initial MAC address from ifconfig command
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    mac_address = re.search(r"ether\s+([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})", result.stdout)
    if mac_address:
        mac_address = mac_address.group(1)
        print("[+] Current MAC address of device " +interface+ " is :  "+mac_address )
    else:
        print("[-] Error: ", result.stderr)


    if(interface in result.stdout ):
        print("*" *80)
        print("[+] Changing MAC address for " + interface)
        if not newMac:
            newMac = input("Enter the new mac address: ")
        if re.match(pattern, newMac):
                print("[+] "+newMac+" is valid")
                print("*" *80)
                #executing commands in terminal
                subprocess.call(["sudo","ifconfig",interface,"down"])
                subprocess.call(["sudo","ifconfig",interface,"hw","ether",newMac])
                subprocess.call(["sudo","ifconfig",interface,"up"])

                #Obtaining MAC address from ifconfig command to verify output
                result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
                mac_address = re.search(r"ether\s+([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})", result.stdout)
                if mac_address:
                    mac_address = mac_address.group(1)
                    print("[+] The MAC address of device " +interface+ " is updated to: "+mac_address+" successfully")
                else:
                    print("[-] Error: ", result.stderr)
                    return

                print("*" *80)
        else:
            print("[-] Invalid MAC address (invalid characters or format): ", newMac)
            return
    else: 
        print("[-] Invalid interface identifier")
        return
        # sys.exit("Exiting program: Invalid interface entered.") # Exit the program with an error message

#calling changeMac
changeMac()
