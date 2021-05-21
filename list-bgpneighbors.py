from vspk import v6 as vspk
import sys
import inspect
session = vspk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://10.5.0.211:8443')

try:
    session.start()
except:
    print ('ERROR: Failed to start the session')
##..
csprootSession = session.user

csprootSession.subnets.fetch()
##..

mysubnet = csprootSession.subnets.get_first(filter="name == 'subnet001'")
print (mysubnet)
mybgpn = mysubnet.bgp_neighbors.get()
for temp in mybgpn:
    print (temp.name + " " + temp.id)
#..

