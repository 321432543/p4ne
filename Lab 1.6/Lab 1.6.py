import ipaddress as ia
import glob
import re


def function(str):
    interface = re.match("interface (.+)", str)
    if interface:
        return {"int": interface.group(1)}
    host = re.match("hostname (.+)", str)
    if host:
        return {"host": host.group(1)}
    return {}

folder  = glob.glob("C:\Files\p4ne_training\config_files\*.txt")
ipaddr = []
interface = []
hosts = []

for i in folder:
    with open(i) as f:
        for l in f:
            str = function(l)
            if (l.find("ip address") >= 1) & (l.find(".") >= 3):
                l = l.strip()
                l = l.replace("ip address", "")
                ipaddr.append(l)
            if "int" in str:
                interface.append(str)
            if "host" in str:
                hosts.append(str)
print(ipaddr)
print(interface)
print(hosts)