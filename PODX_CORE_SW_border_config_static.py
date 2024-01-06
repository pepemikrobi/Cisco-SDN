import sys

if len(sys.argv) != 3:
    print ("""Usage:
    PODX_CORE_SW_border_config_static.py <pod_number> <core_sw_number>
    
    ex. PODX_R1R2_border_config_static 5 2 (for POD5, CORE_SW2)""")
    exit(1)

pod = sys.argv[1]
core = sys.argv[2]

if ((int(pod) < 1) or (int(pod) >5)):
    print ("<pod_number> must be from 1 to 5")
    exit (1)

if ((int(core) < 1) or (int(core) >2)):
    print ("<core_sw_number> must be either 1 or 2")
    exit (1)

vlan1 = f'30{pod}1' if (int(core) == 1) else f'30{pod}3'
vlan2 = f'30{pod}2' if (int(core) == 1) else f'30{pod}4'

my1 = f'1.1.{pod}.2' if (int(core) == 1) else f'1.1.{pod}.10'
peer1   = f'1.1.{pod}.1' if (int(core) == 1) else f'1.1.{pod}.9'
my1v6 = f'1:1:{pod}::2' if (int(core) == 1) else f'1:1:{pod}::A'
peer1v6 = f'1:1:{pod}::1' if (int(core) == 1) else f'1:1:{pod}::9'

my2 = f'1.1.{pod}.6' if (int(core) == 1) else f'1.1.{pod}.14'
peer2   = f'1.1.{pod}.5' if (int(core) == 1) else f'1.1.{pod}.13'
my2v6 = f'1:1:{pod}::6' if (int(core) == 1) else f'1:1:{pod}::E'
peer2v6 = f'1:1:{pod}::5' if (int(core) == 1) else f'1:1:{pod}::D'

print ("")
print (f"vlan {vlan1}")
print (f" name POD{pod}_R{core}_VN1")
print ("!")
print ("vlan " + vlan2)
print (f" name POD{pod}_R{core}_VN2")
print ("!")
print (f"interface Gi1/{pod}")
print (f" switchport trunk allowed vlan {vlan1},{vlan2}")
print ("!") 
print (f"interface Vlan {vlan1}")
print (f" ip address {my1} 255.255.255.252")
print (f" ipv6 address {my1v6}/126")
print (" no shutdown")
print ("!")
print (f"interface Vlan {vlan2}")
print (f" ip address {my2} 255.255.255.252")
print (f" ipv6 address {my2v6}/126")
print (" no shutdown")
print ("!")
print ("router bgp 65001")
print (f" neighbor {peer1} remote-as 6550{pod}")
print (f" neighbor {peer2} remote-as 6550{pod}")
print (f" neighbor {peer1v6} remote-as 6550{pod}")
print (f" neighbor {peer2v6} remote-as 6550{pod}")
print (" !")
print (" address-family ipv4 unicast")
print (f"  neighbor " + peer1 + " default-originate")
print (f"  neighbor " + peer2 + " default-originate")
print (" !")
print (" address-family ipv6 unicast")
print (f"  neighbor " + peer1v6 + " activate")
print (f"  neighbor " + peer1v6 + " default-originate")
print (f"  neighbor " + peer2v6 + " activate")
print (f"  neighbor " + peer2v6 + " default-originate")
print
