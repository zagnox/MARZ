# MARZ - MAC Address Randomization by Zagnox
Changing the MAC address every time you power up your linux is a pain. Sometimes you might even
forget to do so. 

MARZ is a simple script that changes the MAC address to a truly random one each time 
you connect to a network. 

You simply need to run this python script once to create a file in 
NetworkManager directory which changes the MAC address everytime you connect into a network.
If at some point you do not want this functionality simply delete the created file at
`/etc/NetworkManager/conf.d/00-macrandomize.conf`

## Usage
Clone the repository `git clone https://github.com/zagnox/MARZ`

cd inside the repo `cd /Marz`

Run the script as superuser `sudo python3 marz.py`

### Check if the MARZ is working on your device

Run `ip a` in your linux terminal. if link/ether and permaddr are different values then the configuration is successful.

You can also disconnect and reconnect to your network. Run `ip a` again and see a different MAC address under link/ether.
