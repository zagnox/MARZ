# MAC Address Randomization by Zagnox
#
# This is a simple python script which creates a file
# in NetworkManager directory. It appends a few lines
# to the file to randomize the MAC address every time
# you connect to a network. After running the script
# once, you don't have to manually change the MAC
# using tools such as macchanger.

file_path = '/etc/NetworkManager/conf.d/00-macrandomize.conf'
file_content = """[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=random
ethernet.cloned-mac-address=stable
connection.stable-id=${CONNECTION}/${BOOT}"""

try:
    with open(file_path, 'a') as file:
        file.write(file_content)
    print("File created successfully to ", file_path)
except PermissionError:
    print("Permission denied. Run as superuser or with appropriate permissions.")
except Exception as e:
    print("An error occurred: ", str(e))
