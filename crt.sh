#!/usr/bin/env perl
# Description: Get the subdomains from a HTTPS website in a few secs
# Depends on:  p5-json
#
# (c) 2020 Alexandr Savca, alexandr dot savca89 at gmail dot com

use strict;
use warnings;
#use diagnostics;
use feature 'say';
use HTTP::Tiny;
use File::Basename;
use JSON;

my $program = basename $0;
my $domain = shift;
if (!length $domain || $domain =~ /^--?(?:h|help)$/) {
    print <<"EOF";
Usage: $program <domain without www.>
Get the subdomains from a HTTPS website in a few seconds.

$program does not use neither dictionary attack nor brute-force, it
just abuses of Certificate Transparency logs.

For more information about CT logs, check
https://www.certificate-transparency.org and https://crt.sh
EOF
    exit 1;
}

my $response = HTTP::Tiny->new->get(
    "https://crt.sh/?q=$domain&output=json"
);

die "Failed!\n"     unless        $response->{success};
die "No content!\n" unless length $response->{content};

my $json = decode_json $response->{content};
my @subs = map { split /\s+/, $_->{name_value} } @$json;
my %uniq = map { $_ => 1 } @subs;
say for sort keys %uniq;

# vim:sw=4:ts=4:sts=4:et:tw=71:cc=72
# End of file.
