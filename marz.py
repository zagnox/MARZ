# MAC Address Randomization by Zagnox
#
# This is a simple python script which creates a file
# in NetworkManager directory. It appends a few lines
# to the file to randomize the MAC address every time
# you connect to a network. After running the script
# once, you don't have to manually change the MAC
# using tools such as macchanger.

import subprocess


file_path = '/home/zagnox/Desktop/test.txt'
file_content = """[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=random
ethernet.cloned-mac-address=stable
connection.stable-id=${CONNECTION}/${BOOT}"""

# creating the file at NetworkManager directory
def create_file(path, content):
    try:
        with open(path, 'a') as file:
            file.write(content)
        print("File created successfully to ", path)
    except PermissionError:
        print("Permission denied. Run as superuser or with appropriate permissions.")
    except Exception as e:
        print("An error occurred: ", str(e))

# restarting the NetworkManager
def restart_network_manger():
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'NetworkManager'], check=True)
        print("NetworkManager restarted succesfully")
    except subprocess.CalledProcessError as e:
        print("Failed to restart NetworkManager: ", str(e))
        print("You can restart NetworkManager manually on your terminal 'sudo systemctl restart NetworkManager'")

create_file(file_path, file_content)
restart_network_manger()
