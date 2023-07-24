crypt
=====

Disk encryption configuration.

systemd: crypttab
-----------------

``/etc/crypttab`` requires systemd.

Options
^^^^^^^

 - ``luks``: encrypted with LUKS
 - ``discard``: enable fstrim
 - ``initramfs``: mount during initramfs (rootfs)
 - ``plain``: use plain dmcrypt
 - ``swap``: create swap filesystem on the block device

Configurations
^^^^^^^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/crypttab

   system	UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX	none		luks,discard,initramfs
   swap		/dev/mapper/XXXX				/dev/urandom	plain,discard,cipher=aes-cbc-essiv:sha256,size=256,swap

Rootfs: decrypt LUKS partition during initramfs, enable trim.

SWAP: use a random encryption key, format as swap, enable trim.

OpenRC: dmcrypt
---------------

Configure SWAP
^^^^^^^^^^^^^^

Dependencies:
 - Gentoo: ``sys-fs/cryptsetup``
 - Alpine: ``blkid cryptsetup cryptsetup-openrc``

.. code-block:: unixconfig
   :caption: /etc/conf.d/dmcrypt

   swap=crypt-swap
   source='/dev/disk/by-partuuid/XXXX'

.. code-block:: console
   :caption: load at boot

   # rc-update add swap boot
   # rc-update add dmcrypt boot
