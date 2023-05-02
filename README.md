**Change MAC Address**

    This script is designed to change the MAC address of a specified network interface on a Linux system. The user can specify the network interface and the new MAC address through command-line arguments. If the new MAC address is not provided, the user will be prompted to enter it.

**Prerequisites**

**~**   Python 3
**~**   Linux system

**How to use**

    Command-line options:
    
-i or --interface: specify the interface for which the MAC address needs to be changed.
-m or --macAddress: specify the new MAC address in the format XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX.

**Running the script**

Open a terminal window.
Navigate to the directory where the script is located.
Type python3 machanger.py followed by the command-line options.
Example:
**
**~**   python3 macChanger.py --interface eth0 --macAddress 12:34:56:78:90:ab
**~**   python3 macChanger.py -i eth0 -m 12:34:56:78:90:ab
**
The script will disable the specified interface, change the MAC address to the new one, and then enable the interface again. The new MAC address will be verified by executing the ifconfig command and displaying the output.

Note: The script requires root privileges to execute the ifconfig command. Therefore, it must be run with sudo.
