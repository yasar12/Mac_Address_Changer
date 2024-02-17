import subprocess
import argparse
import re
def get_user_input():
    parse_object = argparse.ArgumentParser()
    parse_object.add_argument("-i","--interface", dest="interface", help="interface to change")
    parse_object.add_argument("-m","--mac", dest="mac", help="new mac address")

    return  parse_object.parse_args()


def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(user_interface):
    ifconfig=subprocess.check_output(["ifconfig",user_interface])
    new_mac=re.search(r"ether (\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)",ifconfig.decode("utf-8"))
    if new_mac:
        return new_mac.group(1)
    else:
        return None


print("Mac Address Changer started")
user_input = get_user_input()

change_mac_address(user_input.interface,user_input.mac)
final_mac=control_new_mac(user_input.interface)
if final_mac==user_input.mac:
    print("Successfully changed mac address")
else:
    print("Mac address not changed")