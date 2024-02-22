import json

with open('data.json') as f:
    j = json.load(f)


print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

ai = j['imdata']

for i in ai:
    a1 = i["l1PhysIf"]
    a2 = a1["attributes"]
    dn = a2['dn']
    s = a2['speed']
    m = a2['mtu']
    c = ""
    if(dn != "topology/pod-1/node-201/sys/phys-[eth1/33]"):
        if(dn != "topology/pod-1/node-201/sys/phys-[eth1/34]"):
            if(dn != "topology/pod-1/node-201/sys/phys-[eth1/35]"):
                continue
    if(len(dn) == 42):
        c += dn + " " * 30 + s + "   " + m
    else:
        c += dn + " " * 31 + s + "   " + m
    print(c)