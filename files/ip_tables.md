# IP Tables
I was having trouble connecting to local network computers while connected to the ICG OpenVPN server.

Run `route print` to get a listing of the IP routing.

```
=======================================================================
Interface List
0x1 ........................... MS TCP Loopback interface
0x2 ...00 10 a4 8b 4b 8e ...... Intel(R) PRO/100+ MiniPCI - Packet Scheduler Miniport
0x4 ...44 45 53 54 42 00 ...... Nortel IPSECSHM Adapter - Packet Scheduler Miniport
0x20003 ...00 04 5a 0c 96 db ...... Instant Wireless - Network PC CARD #2 - Packet Scheduler Miniport
=======================================================================
=======================================================================
Active Routes:
Network Destination     Netmask       Gateway     Interface Metric
        0.0.0.0         0.0.0.0   192.168.1.1 192.168.1.100     30
      127.0.0.0       255.0.0.0     127.0.0.1     127.0.0.1     1
    192.168.1.0   255.255.255.0 192.168.1.100 192.168.1.100     30
  192.168.1.100 255.255.255.255     127.0.0.1     127.0.0.1     30
  192.168.1.255 255.255.255.255 192.168.1.100 192.168.1.100     30
      224.0.0.0       240.0.0.0 192.168.1.100 192.168.1.100     30
255.255.255.255 255.255.255.255 192.168.1.100             2     1
255.255.255.255 255.255.255.255 192.168.1.100 192.168.1.100     1
255.255.255.255 255.255.255.255 192.168.1.100             4     1
Default Gateway:       192.168.1.1
=======================================================================
Persistent Routes:
None
```
`route \[-p\] add <destination> mask <subnet mask> <gateway> metric <lowest number wins> if <interface>`

`route -p add 0.0.0.0 mask 0.0.0.0 192.168.1.1 metric 1 if 0x20003`

- http://www.itprotoday.com/management-mobility/q-when-i-add-static-ip-route-what-value-do-i-use-interface
