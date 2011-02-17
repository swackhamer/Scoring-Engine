#!/usr/bin/python

import sys
import dns.resolver
import dns.rdatatype
import dns.rdataclass
import subprocess

def get_A_record(dns_ip, dns_name):
	a = dns.resolver.get_default_resolver()
	answers = a.query(dns_name, dns.rdatatype.A, dns.rdataclass.IN, False, None)

	# Set the DNS server to query
	a.nameservers = dns_ip	

	IPs = []

	for rdata in answers:
		IPs.append(rdata.address)

	return IPs

if __name__ == '__main__':
	print get_A_record('8.8.8.8', 'youtube.com')
