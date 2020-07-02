import ipaddress as ia
import random

class IPv4RandomNetwork(ia.IPv4Network):

    def __init__(self, n, p):
        ia.IPv4Network.__init__(self, (random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)


    def regular(self):
        return not (self.is_multicast | self.is_loopback | self.is_reserved | self.is_private | self.is_unspecified)

    def keyFunc(self):
        a = int(self.network_address)
        m = int(self.netmask)
        return m * 2**32 + a


def sortfunc(x):
    return x.keyFunc()

random.seed()

net_list = []

while len(net_list) < 50:
    net = IPv4RandomNetwork(8, 24)
    if net.regular() and net not in net_list:
        net_list.append(net)

for a in sorted(net_list, key=sortfunc):
    print(a)

