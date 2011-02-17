#!/usr/bin/python

import sys
try:
	import dns.resolver
	import dns.rdatatype
	import dns.rdataclass
except ImportError:
	print 'Need dnspython module located at : http://www.dnspython.org'
	sys.exit()
import signal

def get_A_record(dns_ip, dns_name, timeout=2):
	a = dns.resolver.get_default_resolver()

	# Set the DNS server to query
	ns = []
	ns.append(dns_ip)
	a.nameservers = ns	

	def handler(signum, frame):
		raise IOError	

	signal.signal(signal.SIGALRM, handler)

	# Set alarm to timeout in seconds so DNS query returns 0.0.0.0 if it fails
	signal.alarm(timeout)

	try:	
		answers = a.query(dns_name, dns.rdatatype.A, dns.rdataclass.IN, False, None)
	except IOError:
		return '0.0.0.0'

	signal.alarm(0)
	
	IPs = []
	for rdata in answers:
		IPs.append(rdata.address)

	return IPs

if __name__ == '__main__':
	print get_A_record('192.168.1.1', 'google.com')
