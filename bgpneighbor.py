from vspk import v6 as vspk
import sys
import inspect
import argparse
session = vspk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://10.5.0.211:8443')

### Add arguments to vars
parser = argparse.ArgumentParser()
parser.add_argument(dest='operation', choices=[ 'create', 'list' ])
parser.add_argument('-s', '--subnet', type=str, help="Subnet ID" )
parser.add_argument('-n', '--bgpneighbor', type=str, help="BGP Neighbor name" )
parser.add_argument('-a', '--peer_as', type=str, help="Peer AS" )
parser.add_argument('-i', '--peer_ip', type=str, help="Peer IPv4" )
parser.add_argument('-b', '--session', type=str, help="Session" )
args = parser.parse_args()

try:
    session.start()
except:
    print ('ERROR: Failed to start the session')
##..

try:
    file = open(args.session)
    blob = file.read().replace("\n", " ")
    file.close()
except:
    print ('ERROR: Failed to open XML file with session blob')

csprootSession = session.user
mysubnet = csprootSession.subnets.get_first(filter="ID == " + "'" + args.subnet + "'")
print (mysubnet)

## List subnets
if args.operation == "list" :
    mybgpneighbors = mysubnet.bgp_neighbors.get()
    for temp in mybgpneighbors:
        print (temp.name)
#..

if args.operation == "create" :
    mybgpneighbor = vspk.NUBGPNeighbor(name=args.bgpneighbor,peer_as =args.peer_as, peer_ip=args.peer_ip, session=blob)
    mysubnet.create_child(mybgpneighbor)
    print (mybgpneighbor)
  
#..
