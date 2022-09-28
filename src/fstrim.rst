fstrim (SSD)
============

fstrim: tell the SSD's firmware of unused blocks on the filesystem
Different implementation between util-linux and busybox.
Does not works with swap devices or ZFS pools.

util-linux and cron
-------------------

.. code-block:: console

   # printf '#!/bin/sh\nfstrim -a "$@"\n' >/etc/cron.weekly/fstrim
   # chmod 755 /etc/cron.weekly/fstrim
   # /etc/cron.weekly/fstrim -v

busybox and Alpine
------------------

`fs` variable: list of filesystems to trim

.. code-block:: console

   # fs='/ /boot/efi'
   # printf '#!/bin/sh\nret=0\nfor fs in %s\ndo\n\tfstrim "$@" "${fs}" || ret=1\ndone\nexit "${ret}"\n' "$fs" >/etc/periodic/weekly/fstrim
   # chmod 755 /etc/periodic/weekly/fstrim
   # /etc/periodic/weekly/fstrim -v

swap
----

Use ``discard=once`` to discard the whole swap once at boot,
or ``discard=pages`` to discard freed swap pages, or ``discard`` for both.
I think ``discard=pages`` may be overkill for a swap area, which is generaly
small compared to the drive size and not used too often.

.. code-block:: unixconfig
   :caption: /etc/fstab

   XXXX	none	swap	sw,discard=once		0 0

ZFS
---

Either regularly run ``zpool trim POOL``,
or enable auto-trim with ``zpool set autotrim=on POOL``.
