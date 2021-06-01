#Some guidelines

You can use python <<app.py>> --help any time to see the arguments
 
Remember to change the connection data in every file. I would try to do a global file later for the connection info.
session = vspk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://10.5.0.211:8443')

##Routing Policies
List policies in the Enterprise
```
[stack@undercloud docker-python]$ python rpolicy.py list -e OpenStack_default
ERROR: Failed to open XML file with session blob
Looking into Enterprise: 'OpenStack_default' with ID:07ff47ec-55ee-11eb-a4b9-07c0606f7f2c
export_subnets ID: f0636173-a2e4-11eb-b895-abee2be05662
test_in ID: 84ae54cc-ba66-11eb-b895-fd0d453f0957
test_out ID: 885eb2f6-ba66-11eb-b895-b76269419904
```
 
To change action and the blob in the routing policy:
```
[stack@undercloud docker-python]$ python rpolicy.py update -e OpenStack_default -a REJECT -b blob.xml -r 84ae54cc-ba66-11eb-b895-fd0d453f0957
Looking into Enterprise: 'OpenStack_default' with ID:07ff47ec-55ee-11eb-a4b9-07c0606f7f2c
test_in ID:84ae54cc-ba66-11eb-b895-fd0d453f0957
```
(blob.xml is a file, you can see an example in the github repo, you can change it an update it thru this command line)

 
##Create Subnet and Zone
 
List Subnets
```
[stack@undercloud docker-python]$ python subnet.py subnetlist -d vsd_managed_01
BGP Peering Net 192-168-100 ID:54e847e8-9e16-11eb-b895-971e13a886a3
Noadvertised_Subnet ID:aa49fa63-a2e4-11eb-b895-dddb044426f2
subnet001 ID:78027957-ba50-11eb-b895-856bcd038717
subnet002 ID:86f23373-ba72-11eb-b895-83058a8b5958
vsd_managed_sub01 ID:704c503f-75e2-11eb-a4b9-79a63421a42a
```
(Specify domain with -d)
 
 
Create a zone:
```
[stack@undercloud docker-python]$ python subnet.py zonecreate -d vsd_managed_01 -z zonetest01
<class 'vspk.v6.nuzone.NUZone'> (ID=4355b3a6-ba72-11eb-b895-71946d9de502)
 ```
Create a subnet
```
[stack@undercloud docker-python]$ python subnet.py subnetcreate -d vsd_managed_01 -z zonetest01 -s subnet002 -a 192.168.253.0 -n 255.255.255.0 -g 192.168.253.1 -x "this is a test"
<class 'vspk.v6.nusubnet.NUSubnet'> (ID=86f23373-ba72-11eb-b895-83058a8b5958)
```
