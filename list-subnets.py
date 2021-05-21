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

csprootSession.domains.fetch()
##..

mydomain = csprootSession.domains.get_first(filter="name == 'vsd_managed_01'")
print (mydomain)
mysubnets = mydomain.subnets.get()
for temp in mysubnets:
    print (temp.name + " " + temp.id)
#..

