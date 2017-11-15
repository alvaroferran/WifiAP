Wifi Access Point
====================

These instructions to create an Access Point are based on the ones found at [elinux.org](https://elinux.org/RPI-Wireless-Hotspot#Instructions)

<img align="center" src="tree.png" >

Once the files have been copied and the SSID and password changed the following command must be executed

	
	sudo ifconfig wlan0 192.168.42.1 && sudo service hostapd start && sudo service udhcpd start
