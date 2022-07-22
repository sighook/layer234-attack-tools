Layer 2/3/4 attack tools
========================

## Description:

Set of tools and helpers for attacks on the 2, 3 and 4 levels of the OSI Model.
Some of them I adapted from the Net, some I wrote myself, some by [volgk](https://github.com/volgk).

Enjoy.

| Name                   | Description                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------- |
| arp-mac-spoof          | Perform CAM overflow attack on Layer2 switches.                                    |
| arp-spoof-flood        | Spoof ARP reply.                                                                   |
| dhcp-spoof-shock       | Spoof a DHCP server and exploit all clients vulnerable to the 'ShellSock' attacks. |
| gateway-finder         | Identify routers on the local LAN and paths to the Net.                            |
| icmp-spoof-reply       | ICMP spoof reply.                                                                  |
| mac2manuf              | Find the manufacturer by MAC address.                                              |
| magpie                 | Find LEAP/MSCHAPv2/PPP/PPTP/RADIUS sensitive data in pcap files.                   |
| netxml-dump            | Dump aircrack's netxml output in pretty format.                                    |
| traceroute-geolocation | Traceroute to host with geolocation info.                                          |
| ---------------------- | ---------------------------------------------------------------------------------- |

## Dependencies:

- aircrack-ng
- nmap
- perl and XML::Simple module
- scapy
- wireshark (tshark)

## See also

- [yersinia](https://github.com/tomac/yersinia) - Framework for layer 2 attacks.
- [layer567_attack_tools](https://github.com/chinarulezzz/layer567_attack_tools) - Layer 5, 6 and 7 attack tools.

<!-- End of file. -->
