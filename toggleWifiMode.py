#!/usr/bin/python

import os


def toggleComment(string):
    if string.startswith("#"):
        return string[1:]
    else:
        return "#"+string


def hostapd():
    lineHostapd = "DAEMON_CONF="
    with open("/etc/default/hostapd", "r") as fileIn:
        with open("/etc/default/hostapd2", "w") as fileOut:
            for line in fileIn:
                if lineHostapd in line:
                    line = toggleComment(line)
                    fileOut.write(line)
                else:
                    fileOut.write(line)
    os.rename("/etc/default/hostapd2", "/etc/default/hostapd")


def udhcpd():
    lineUdhcpd = "DHCPD_ENABLED="
    with open("/etc/default/udhcpd", "r") as fileIn:
        with open("/etc/default/udhcpd2", "w") as fileOut:
            for line in fileIn:
                if lineUdhcpd in line:
                    line = toggleComment(line)
                    fileOut.write(line)
                else:
                    fileOut.write(line)
    os.rename("/etc/default/udhcpd2", "/etc/default/udhcpd")


def interfaces():
    lineClient = "#CONNECT TO WIFI NETWORK"
    lineAp = "#CREATE ACCESS POINT"
    numClient = 10000
    numAp = 10000
    with open("/etc/network/interfaces", "r") as fileIn:
        with open("/etc/network/interfaces2", "w") as fileOut:
            for numLine, line in enumerate(fileIn):
                if line.startswith(lineClient):
                    numClient = numLine
                if line.startswith(lineAp):
                    numAp = numLine
                if numLine > numClient and numLine <= numClient+5:
                    line = toggleComment(line)
                    fileOut.write(line)
                if numLine > numAp and numLine <= numAp+4:
                    line = toggleComment(line)
                    fileOut.write(line)
                elif not (numLine > numClient and numLine <= numClient+5)   \
                        and not (numLine > numAp and numLine <= numAp+4):
                    fileOut.write(line)
    os.rename("/etc/network/interfaces2", "/etc/network/interfaces")

hostapd()
udhcpd()
interfaces()
os.system('reboot')
