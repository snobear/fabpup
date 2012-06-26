fabpup
======

A simple library to access the Puppet REST API with Fabric

Fabpup consists of a single py file that you "include" in your fabfile.py and gives you a simple way to set Fabric's
env.hosts lists with a list of hosts from Puppet based on a dictionary of facts to match on.    

Usage:
------

```python
import fabpup

# settings - see fabpup.py for available settings
fabpup['host'] = 'puppet.example.com'   # your puppetmaster host

# create a dict with facts to match on
myfacts = {'facts.operatingsystem':'CentOS',
           'facts.lsbdistrelease':'6.2'
	         }

# return a list of hosts for Fabric
env.hosts = get_hosts_by_facts(myfacts)
```

Dependencies
------------

You'll need the "Requests: HTTP for Humans" module:  http://docs.python-requests.org/en/latest/index.html

Notes:
------

Yes, not much to it.  It only has support for the "facts_search" feature of the Puppet REST API, but I have plans
to add everything else.  Please fork if you're interested in helping out.