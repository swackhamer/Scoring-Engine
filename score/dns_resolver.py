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

def get_MX_record(dns_ip, dns_name, timeout=.5):
    a = dns.resolver.get_default_resolver()

    # Set the DNS server to query
    ns = []
    ns.append(dns_ip)
    a.nameservers = ns
    
    a.lifetime = timeout
    
    try:
        answers = a.query(dns_name, dns.rdatatype.MX, dns.rdataclass.IN, False, None)
    except:
        return '-1'

    IPs = []
    for rdata in answers:
        IPs.append(rdata.exchange)

    return IPs

def get_A_record(dns_ip, dns_name, timeout=.5):
    a = dns.resolver.get_default_resolver()

    # Set the DNS server to query
    ns = []
    ns.append(dns_ip)
    a.nameservers = ns
    
    #set lifetime to timeout seconds
    a.lifetime = timeout
    
    try:
        answers = a.query(dns_name, dns.rdatatype.A, dns.rdataclass.IN, False, None)
    except:
        return '-1'


    IPs = []
    for rdata in answers:
        IPs.append(rdata.address)

    return IPs

if __name__ == '__main__':
    print get_A_record('192.168.1.1', 'google.com')
    print get_MX_record('192.168.1.1', 'gmail.com')
