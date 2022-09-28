init
====

OpenRC
------

Common configuration
^^^^^^^^^^^^^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/rc.conf

   rc_parallel="YES"
   rc_shell=/sbin/sulogin
   rc_logger="YES"
   unicode="YES"
   rc_tty_number=12
   rc_cgroup_mode="unified"

Note: Alpine may not support cgroup v2 (unified mode).

Other configurations
^^^^^^^^^^^^^^^^^^^^

 - `rc_fuser_timeout=30`: customize timeout for fuser remote filesystems

If you require `/usr/*bin` to take precedence over `/*bin` in `PATH`, add:

.. code-block:: unixconfig
   :caption: /etc/rc.conf

   PATH="/lib/rc/sbin:/lib/rc/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH}"

Services
^^^^^^^^

Volatile or read-only rootfs:
 - `rc-update del savecache shutdown`

systemd
-------

journald
^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/systemd/journald.conf

   [Journal]
   SystemMaxUse=1G

Configurations:

 - ``SystemMaxUse``: maximum space used by log files

logind
^^^^^^

.. code-block:: unixconfig
   :caption: /etc/systemd/logind.conf

   [Login]
   KillUserProcesses=yes
   KillExcludeUsers=root
   HandlePowerKey=poweroff
   HandleSuspendKey=ignore
   HandleHibernateKey=ignore
   HandleLidSwitch=ignore
   HandleLidSwitchExternalPower=ignore
   HandleLidSwitchDocked=ignore
   HandleRebootKey=reboot

Configurations:

 - ``KillUserProcesses``: configure if user process should be killed
   on user logout
