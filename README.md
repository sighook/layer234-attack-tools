Layer 2/3/4 attack tools
========================

## Description:

Set of tools and helpers for attacks on the 2, 3 and 4 layers of the OSI Model.
Some of them I adapted from the Net, some I wrote myself, some by [volgk](https://github.com/volgk).

Enjoy.

| Name                   | Description                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------- |
| arp_mac_spoof.py       | Perform CAM overflow attack on Layer2 switches.                                    |
| arp_spoof_flood.py     | Spoof ARP reply.                                                                   |
| dhcp_spoof_shock.py    | Spoof a DHCP server and exploit all clients vulnerable to the 'ShellSock' attacks. |
| gateway_finder.py      | Identify routers on the local LAN and paths to the Net.                            |
| icmp_spoof_reply.py    | ICMP spoof reply.                                                                  |
| mac2manuf.pl           | Find the manufacturer by MAC address.                                              |
| magpie.sh              | Find LEAP/MSCHAPv2/PPP/PPTP/RADIUS sensitive data in pcap files.                   |
| netxml_dump.pl         | Dump aircrack's netxml output in pretty format.                                    |
| traceroute_geoloc.sh   | Traceroute to host with geolocation info.                                          |

## Dependencies:

- aircrack-ng
- nmap
- perl and XML::Simple module
- scapy
- wireshark (tshark)

## See also

- [yersinia](https://github.com/tomac/yersinia) - Framework for layer 2 attacks.
- [layer567-attack-tools](https://github.com/chinarulezzz/layer567-attack-tools) - Layer 5, 6 and 7 attack tools.

<!-- End of file. -->
