#!/bin/sh
# Description: Enumerate DNS hostnames by brute force guessing of common subdomains
# Depends on:  nmap

if [ -z $1 ] || [ -z $2 ]; then
    cat <<EOF
Enumerate DNS hostnames by brute force guessing of common subdomains.

Usage: [OPTIONS] $(basename $0) <HOST> <WORDLIST>

where OPTIONS are:
      DEBUG=-d     Debug.
      THREADS=N    Threads to use (default 5).
EOF
    return
fi

DEBUG=${DEBUG:-""}
THREADS=${THREADS:-5}

nmap $DEBUG \
    -T4 -p 53 \
    --script dns-brute \
    --script-args dns-brute.threads=$THREADS,dns-brute.hostlist=$2 \
    $1

# vim:sw=2:ts=2:sts=2:et:cc=72
# End of file.
