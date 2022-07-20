#!/usr/bin/env perl
# Description: Checks DNS zone configuration against best practices,
#              including RFC 1912
# Depends on:  nmap p5-net-dns
#
# (c) 2020 Alexandr Savca, alexandr dot savca89 at gmail dot com

BEGIN { $|++ }

use strict;
use warnings;
use Net::DNS;

my $hostname = shift or die <<EOF;
Checks DNS zone configuration against best practices, including
RFC 1912.

Usage: $0 <HOSTNAME>
EOF

my $res  = Net::DNS::Resolver->new;

# Find the nameservers for the domain
my $reply = $res->query($hostname, 'NS');
die 'query failed: ' . $res->errorstring . "\n" unless $reply;

my @nameservers = grep { $_->type eq 'NS' } $reply->answer;
@nameservers    = sort { $a->nsdname cmp $b->nsdname } @nameservers;

my @nsdnames;
push(@nsdnames, $_->nsdname) for @nameservers;

print <<EOF;

Check DNS zone configuration agains best practices, including RFC 1912:

\@DOMAIN       $hostname
\@NAMESERVERS  @nsdnames

EOF

for my $nsd (@nsdnames) {
    my $nsdlen  = length $nsd;
    my $hyphlen = (76 / 2) - $nsdlen;

    print '-' x $hyphlen . "[ $nsd ]" . '-' x $hyphlen . "\n";

    print qx(
        nmap -sn -Pn $nsd --script dns-check-zone \
            --script-args='dns-check-zone.domain=$hostname'
    );

    print "\n";
}

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
