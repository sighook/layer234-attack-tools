#!/usr/bin/env perl
# Description: Dump aircrack's netxml output in pretty format
# Depends on:  p5-xml-simple
#
# (c) 2020 Alexandr Savca, alexandr dot savca89 at gmail dot com

use strict;
use warnings;
no warnings 'uninitialized';
#use diagnostics;
use File::Basename;
use XML::Simple;

my $program = basename $0;

if (!scalar(@ARGV) || $ARGV[0] =~ /^--?(h|help)$/) {
    print <<EOF;
Usage: $program <file.netxml>
Dump aircrack's netxml output in pretty format.
EOF
}

my $has_wireless_clients = 0;
my $xml  = XML::Simple->new;
my $data = $xml->XMLin($ARGV[0]);

print <<"EOH";
FREQMHZ   | CH   | BSSID               | ESSID                           | ENCRYPTION                     | MANUFACTURER
EOH

for my $network (@{ $data->{'wireless-network'} }) {
    my $freqmhz      = $network->{freqmhz};
    my $chan         = $network->{channel};
    my $bssid        = $network->{BSSID};
    my $essid        = $network->{SSID}->{essid}->{content};
    my $encryption   = ref $network->{SSID}->{encryption} ? "@{ $network->{SSID}->{encryption} }" : '';
    my $manuf        = $network->{manuf};

    format AP =
@<<<<<<<< | @<<< | @<<<<<<<<<<<<<<<<<< | @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< | @<<<<<<<<<<<<<<<<<<<<<<<<<<<<< | @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
$freqmhz,   $chan, $bssid,               $essid,                           $encryption,                     $manuf
.

    $~ = 'AP';

    if (ref $network->{'wireless-client'}) {
        print "\n" unless $has_wireless_clients;
        write;
    } else {
        $has_wireless_clients = 0;
        write and next;
    }

    print <<EOH;
                 | CLIENT_MAC          | SSID_PROBES                     | CARRIER                        |
EOH

    my $clients_ref;
    my $client_sep;

    if (ref $network->{'wireless-client'} eq 'HASH') {
        push @$clients_ref, $network->{'wireless-client'};
        $client_sep = '|';
    } elsif (ref $network->{'wireless-client'} eq 'ARRAY') {
        $clients_ref = $network->{'wireless-client'};
    } else {
        die "unknown reference type";
    }

    for my $client (@{ $clients_ref }) {
        my $client_mac   = $client->{'client-mac'};
        my $ssid;
        my $carrier      = $client->{'carrier'};
        my $client_manuf = $client->{'client-manuf'};
        my @ssids;

        format STA =
                 | @<<<<<<<<<<<<<<<<<< | ^<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< | @<<<<<<<<<<<<<<<<<<<<<<<<<<<<< | @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                   $client_mac,          $ssid,                            $carrier,                        $client_manuf
~~                                     | ^<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< |
                                         $ssid
.
        $~ = 'STA';

        write and next if not ref $client->{SSID};

        if (ref $client->{SSID} eq 'HASH') {
            $ssid = $client->{SSID}->{ssid};
        } else {
            $ssid .= "$_->{ssid}\r\n" for @{ $client->{SSID} };
        }

        write;
    }
    print "\n";
    $has_wireless_clients = 1;
}

# vim:sw=4:ts=4:sts=4:et
# End of file.
