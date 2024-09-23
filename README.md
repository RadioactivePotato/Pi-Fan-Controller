# Pi-Fan-Controller [NOT WORKING]

Plug the red wire (positive) of the fan to GPIO pin 27 (Customizable on line 5)

And the black wire (negative) to any ground pin on the pin header

![image](https://github.com/user-attachments/assets/51f797d0-94af-484e-a9f2-70ffd9a02206)


## Make this runs on startup
Create the script in the home directory

Make it executable

```
$ chmod a+x fancontrol.py
```

Add a line to the end of /etc/rc.local to run it when booting up

```
$ sudo nano /etc/rc.local
```

Add this above the line with `exit 0`

`python3 /home/username/fancontrol.py &`

### This is what it should look like

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each mutiuser runlevel.
# Make sure that ethe script will "edit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP Address is %s\n" "$_IP"
fi

python3 /home/username/fancontrol.py &

exit 0
```
