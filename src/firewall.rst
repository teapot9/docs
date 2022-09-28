Firewall
========

Ports numbers:

 - SSH: 22/tcp
 - DNS: 53/udp
 - NTP: 123/udp
 - SMB: 445/tcp+udp
 - iSCSI: 860/tcp, 3260/tcp
 - `KDE Connect <https://kdeconnect.kde.org/>`_: 1714-1764/tcp+udp
 - `distcc <https://www.distcc.org/>`_: 3632/tcp
 - `Avahi mDNS <https://www.avahi.org/>`_: 5353/udp
 - `Syncthing <https://syncthing.net/>`_: 22000/tcp
 - `barrier <https://github.com/debauchee/barrier>`_: 24800/tcp

nftables
--------

.. code-block:: unixconfig
   :caption: /etc/nftables.rules

   #!/sbin/nft -f
   
   flush ruleset
   
   # filter, inet
   table inet filter {
   	chain output {
   		type filter hook output priority 0; policy accept;
   		counter comment "count accepted packets"
   	}
   
   	chain forward {
   		type filter hook forward priority 0; policy drop;
   		counter comment "count dropped packets"
   	}
   
   	chain input {
   		type filter hook input priority 0; policy drop;
   		ct state invalid counter drop comment "drop invalid packets"
   		ct state {established, related} counter accept comment "accept all connections related to connections made by us"
   		iifname lo accept comment "accept loopback"
   		iifname != lo ip daddr 127.0.0.1/8 counter drop comment "drop connections to loopback not coming from loopback"
   		iifname != lo ip6 daddr ::1/128 counter drop comment "drop connections to loopback not coming from loopback"
   		ip protocol icmp counter accept comment "accept all icmp types"
   		ip6 nexthdr icmpv6 counter accept comment "accept all icmp types"
   		tcp dport 22 counter accept comment "accept ssh"
   		udp dport 5353 counter accept comment "accept mdns"
   		counter comment "count dropped packets"
   	}
   }
