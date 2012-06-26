# fabpup: Fabric Interface to Puppet REST API
# Author: Jason Ashby
#
import requests
import ast
import os.path
import sys

#
# Default Settings
#
fabpup = {
    # puppetmaster host
    'host': 'localhost',
    # port for puppet rest API
    'port': 8140,
    # environment
    'environment': 'production',
    # what format to return: pson, yaml
    'return_format': 'pson',
}

#
# Returns a list of hosts matching a set of fact conditions
#
def get_hosts_by_facts(facts=None):
    if facts is None:
        print "ERROR: facts is not defined in gethosts_by_facts."
        sys.exit(1)

    hostlist = []

    headers = {'Accept': fabpup['return_format']}
    requrl = "https://%s:%d/%s/facts_search/search" % (fabpup['host'], fabpup['port'], fabpup['environment'])
    r = requests.get(requrl, headers=headers, params=facts, verify=False)

    # convert unicode string "list" to a python list
    hostlist = [ item.encode('ascii') for item in ast.literal_eval(r.text) ]

    # set hosts in global Fabric "env.hosts" variable
    return hostlist

#
# Returns a list of hosts in a text file containing one host name per line
#
def get_hosts_by_file(filepath):
    try:
       with open(filepath) as f: pass
    except IOError as e:
       print 'ERROR: file does not exist: %s' % filepath

    hostlist = []
    for line in open(filepath):
        # strip line endings
        hostlist.append(line.rstrip('\r\n\t \t'))

    return hostlist
