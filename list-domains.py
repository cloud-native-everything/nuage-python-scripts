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

csprootSession.enterprises.fetch()
for enterprise in csprootSession.enterprises:
    print (enterprise.name)
##..

myent = csprootSession.enterprises.get_first(filter="name == 'OpenStack_default'")
#mydomains = myent.domains.get_first(filter="name == 'CWC_production'")
mydomains = myent.domains.get()
#myvms = mydomains.vms.get()
#print myvms
#for temp in myvms:
#    print temp.name
#    temp.delete()
#print (mydomains)
for temp in mydomains:
    print (temp.name + " " + temp.id)
#..

