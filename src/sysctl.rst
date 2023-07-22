sysctl
======

System configuration
--------------------

 - Auto-reboot on kernel panic: :sysctl:`kernel.panic`
 - Enable :doc:`kernel:admin-guide/sysrq`: :sysctl:`kernel.sysrq`
 - Swappiness: :sysctl:`vm.swappiness`
 - Cache pressure: :sysctl:`vm.vfs_cache_pressure`


.. code-block:: unixconfig
   :caption: /etc/sysctl.conf

   # System configuration
   kernel.panic = 60
   kernel.sysrq = 244

This config reboots 60s after kernel panic, and enables most sysrq
(except debug).

Security configurations
-----------------------

Restrict unprivileged users:

 - :doc:`kernel:admin-guide/sysctl/kernel`

   - :sysctl:`kernel.kptr_restrict`
   - :sysctl:`kernel.perf_event_paranoid`
   - :sysctl:`kernel.yama.ptrace_scope`
   - dev.tty.ldisc_autoload:
     require privileges to load :doc:`kernel:driver-api/tty/tty_ldisc`
   - :sysctl:`kernel.core_uses_pid`: use PID for coredump filename

BPF:

 - :doc:`kernel:admin-guide/sysctl/kernel`

   - :sysctl:`kernel.unprivileged_bpf_disabled`

 - :doc:`kernel:admin-guide/sysctl/net`

   - net.core.bpf_jit_enable
   - net.core.bpf_jit_harden

Filesystem:

 - :doc:`kernel:admin-guide/sysctl/fs`

   - :sysctl:`fs.protected_hardlinks`
   - :sysctl:`fs.protected_symlinks`
   - :sysctl:`fs.protected_fifos`
   - :sysctl:`fs.protected_regular`
   - :sysctl:`fs.suid_dumpable`

Network:

 - :doc:`kernel:networking/ip-sysctl`:

   - net.ipv4.conf.all.accept_redirects
   - net.ipv4.conf.all.accept_source_route
   - net.ipv4.conf.all.log_martians: log packets with bad address
   - net.ipv4.conf.all.rp_filter
   - net.ipv4.conf.all.secure_redirects
   - net.ipv4.conf.all.send_redirects
   - net.ipv4.conf.default.accept_redirects
   - net.ipv4.conf.default.accept_source_route
   - net.ipv4.conf.default.log_martians
   - net.ipv4.conf.default.rp_filter
   - net.ipv4.conf.default.secure_redirects
   - net.ipv4.conf.default.send_redirects
   - net.ipv4.tcp_dsack
   - net.ipv4.tcp_fack
   - net.ipv4.tcp_rfc1337
   - net.ipv4.tcp_sack
   - net.ipv4.tcp_syncookies
   - net.ipv6.conf.all.accept_redirects
   - net.ipv6.conf.all.accept_source_route
   - net.ipv6.conf.default.accept_redirects
   - net.ipv6.conf.default.accept_source_route

.. code-block:: unixconfig
   :caption: /etc/sysctl.conf

   # Restrict unprivileged users
   dev.tty.ldisc_autoload = 0
   kernel.kptr_restrict = 2
   kernel.perf_event_paranoid = 3
   kernel.yama.ptrace_scope = 1
   kernel.core_uses_pid = 1
   
   # BPF
   kernel.unprivileged_bpf_disabled = 1
   net.core.bpf_jit_enable = 1
   net.core.bpf_jit_harden = 2
   
   # Filesystem
   fs.protected_hardlinks = 1
   fs.protected_symlinks = 1
   fs.protected_fifos = 2
   fs.protected_regular = 2
   fs.suid_dumpable = 0
   
   # Network security
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.log_martians = 1
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.all.secure_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.conf.default.accept_redirects = 0
   net.ipv4.conf.default.log_martians = 1
   net.ipv4.conf.default.rp_filter = 1
   net.ipv4.conf.default.secure_redirects = 0
   net.ipv4.conf.default.send_redirects = 0
   net.ipv4.tcp_rfc1337 = 1
   net.ipv4.tcp_syncookies = 1
   net.ipv6.conf.all.accept_redirects = 0
   net.ipv6.conf.default.accept_redirects = 0
   net.ipv4.conf.all.accept_source_route=0
   net.ipv4.conf.default.accept_source_route=0
   net.ipv6.conf.all.accept_source_route=0
   net.ipv6.conf.default.accept_source_route=0
   net.ipv4.tcp_sack=0
   net.ipv4.tcp_dsack=0
   net.ipv4.tcp_fack=0

Hardenning configurations
-------------------------

 - :doc:`kernel:admin-guide/sysctl/kernel`

   - :sysctl:`kernel.dmesg_restrict`
   - :sysctl:`kernel.kexec_load_disabled`

 - :doc:`kernel:admin-guide/LSM/Yama`

   - kernel.yama.ptrace_scope

.. code-block:: unixconfig
   :caption: /etc/sysctl.conf

   # Hardenning
   kernel.dmesg_restrict = 1
   kernel.yama.ptrace_scope = 3
   kernel.kexec_load_disabled = 1

Performance configurations
--------------------------

 - :doc:`kernel:admin-guide/sysctl/net`

   - :sysctl:`net.core.netdev_max_backlog`

 - :doc:`kernel:networking/ip-sysctl`:

   - net.core.somaxconn
   - net.ipv4.tcp_fastopen
   - net.ipv4.tcp_keepalive_time
   - net.ipv4.tcp_mtu_probing

.. code-block:: unixconfig
   :caption: /etc/sysctl.conf

   # Performance
   net.core.netdev_max_backlog = 16384
   net.core.somaxconn = 8192
   net.ipv4.tcp_fastopen = 3
   net.ipv4.tcp_keepalive_time = 600
   net.ipv4.tcp_mtu_probing = 1
