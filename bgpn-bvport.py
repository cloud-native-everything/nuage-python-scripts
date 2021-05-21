from vspk import v6 as vspk
import sys
import inspect
import argparse
session = vspk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://10.5.0.211:8443')

### Add arguments to vars
parser = argparse.ArgumentParser()
parser.add_argument(dest='operation', choices=[ 'create', 'list' ])
parser.add_argument('-s', '--subnet', type=str, help="Subnet ID" )
parser.add_argument('-p', '--bridge_vport', type=str, help="Bridge vPort ID" )
parser.add_argument('-n', '--bgpneighbor', type=str, help="BGP Neighbor name" )
parser.add_argument('-a', '--peer_as', type=str, help="Peer AS" )
parser.add_argument('-i', '--peer_ip', type=str, help="Peer IPv4" )
parser.add_argument( '--policy_in', type=str, help="Routing Policy Import ID" )
parser.add_argument( '--policy_out', type=str, help="Routing Policy Export ID" )
args = parser.parse_args()

try:
    session.start()
except:
    print ('ERROR: Failed to start the session')
##..

csprootSession = session.user
mysubnet = csprootSession.subnets.get_first(filter="ID == " + "'" + args.subnet + "'")
mybvport = mysubnet.vports.get_first(filter="ID == " + "'" + args.bridge_vport + "'")
print (mybvport)

## List subnets
if args.operation == "list" :
    mybgpneighbors = mybvport.bgp_neighbors.get()
    for temp in mybgpneighbors:
        print (temp.name)
#..

if args.operation == "create" :
    mybgpneighbor = vspk.NUBGPNeighbor(name=args.bgpneighbor,peer_as =args.peer_as, peer_ip=args.peer_ip, associated_import_routing_policy_idi=args.policy_in, associated_export_routing_policy_id=args.policy_out )
    mybvport.create_child(mybgpneighbor)
    print (mybgpneighbor)
  
#..
