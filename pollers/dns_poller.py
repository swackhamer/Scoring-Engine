#!/usr/bin/python

import sys
import dns.resolver

if __name__ == '__main__':
    d = dns.resolver('dns/resolver.conf')
    print d
