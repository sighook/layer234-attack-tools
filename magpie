#!/bin/sh
# Description: Find LEAP/MSCHAPv2/PPP/PPTP/RADIUS sensitive data in pcap files
# Depends on:  perl wireshark
#
# (c) 2020 volgk, github.com/volgk
# (c) 2022 Alexandr Savca, alexandr dot savca89 at gmail dot com

usage() {
	cat <<EOF
Usage: ${0##*/} <file.cap>
$(grep -Po '^# Description: \K.*' "$0").
EOF
}

case $1 in
-h|--help)
	usage
	exit 0
	;;
"")
	usage
	exit 1
	;;
*)
	CAPFILE=$1
	if [ ! -f "$CAPFILE" ]; then
		echo "$CAPFILE not found!"
		exit 2
	fi
	;;
esac

prettify() {
	perl -alne '
	next if "@F" eq "[]";
	$F[1]=~s/(..)/$1:/g;
	chop $F[1];
	print "$F[0] => $F[1]";
	'
}

echo "Searching LEAP data..."
tshark  -r "$CAPFILE" -Tfields     \
	-e eap.leap.name           \
	-e eap.leap.peer_challenge \
	-e eap.leap.peer_response  \
	"eap.leap.peer_challenge || eap.leap.peer_response" \
	| prettify

echo "Searching MSCHAPv2 data..."
tshark  -r "$CAPFILE" -Tfields \
	-e chap.name   \
	-e chap.value  \
	-e chap.value  \
	"chap.code == 1 || chap.code == 2" \
	| prettify

echo "Searching PPP data (user|index|challenge)..."
tshark  -r "$CAPFILE" -Tfields     \
	-e chap.name       \
	-e chap.identifier \
	-e chap.value      \
	"chap.code == 2 || chap.code == 1"

echo "Searching RADIUS data (code|id|length|response|authenticator|attributes)"
tshark  -r "$CAPFILE" -Tfields  \
	-e radius.code          \
	-e radius.id            \
	-e radius.length        \
	-e radius.authenticator \
	-e radius.State         \
	"radius"

# End of file.
