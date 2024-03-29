#!/bin/sh
# Description: Traceroute to host with geolocation info
# Depends on:  nmap

usage() {
  cat <<EOF
Usage: ${0##*/} <host> [nmap_arg]...
$(grep -Po '^# Description: \K.*' "$0").
EOF
}

case $1 in
-h|--help)  usage ; exit 0 ;;
"")         usage ; exit 1 ;;
esac

# shellcheck disable=SC2068
/usr/bin/nmap --traceroute --script traceroute-geolocation $@

# vim:sw=2:ts=2:sts=2:et:tw=71:cc=72
# End of file.
