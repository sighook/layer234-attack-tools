#!/usr/bin/env perl
# Description: Find the manufacturer by MAC address
# Depends on:  aircrack-ng
#
# (c) 2020 Alexandr Savca, alexandr dot savca89 at gmail dot com

use strict;
use warnings;
use File::Basename;

my $program = basename $0;
my $arg = shift;

sub usage {
    print <<EOF;
Usage: $program MAC
Find the manufacturer by MAC address.
EOF
}

usage() and exit(0) if $arg && $arg =~ /^--?(h|help)$/;
usage() and exit(1) if !$arg;

my @oct = split /:/, $arg;
my $oui = '/etc/aircrack-ng/airodump-ng-oui.txt';

die "missing $oui: run airodump-ng-oui-update!\n" unless -f $oui;

open(my $fh, $oui);
/$oct[0]-$oct[1]-$oct[2] /i and print while <$fh>;
close $fh;

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
