from vspk import v6 as vspk
import sys
import inspect
import argparse
session = vspk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://10.5.0.211:8443')

### Add arguments to vars
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--enterprise', type=str, help="Enterprise Name" )
#parser.add_argument('-d', '--domain', type=str, help="Domain Name" )
args = parser.parse_args()

try:
    session.start()
except:
    print ('ERROR: Failed to start the session')
##..

csprootSession = session.user
csprootSession.enterprises.fetch()

## List domains
myent = csprootSession.enterprises.get_first(filter="name == " + "'" + args.enterprise + "'")
#myent = csprootSession.enterprises.get_first(filter="name == 'OpenStack_default'" )
mydomains = myent.domains.get()
for temp in mydomains:
    print (temp.name)
#..

