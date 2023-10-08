fstab
=====

Options
-------

Common options:

 - access time update (always updated when mtime or ctime changes):

   - ``relatime``: once a day
   - ``lazytime``: always updated in RAM, updated once a day on device
   - ``noatime``: never

 - ``ro``: read-only
 - ``noauto``: don't mount at boot
 - ``user``: allow unprivileged users to mount

Hardenning options:

 - ``nodev``: do not allow device file creation
 - ``nosuid``: do not respect SUID bit permission
 - ``noexec``: do not allow execution of any file

Systemd:

 - ``_netdev``: indicates the mount requires networking
 - ``x-systemd.requires=iscsid.service``: indicates service dependency
 - ``x-systemd.mount-timeout=30``

BTRFS:

 - ``ssd``: SSD optimisations
 - ``compress=zstd``: enable ZSTD transparent compression

CIFS:
 - ``uid`` and ``gid``: set ownership of all the files
 - ``file_mode`` and ``dir_mode``: set permissions of all the files
 - ``mfsymlinks``: enable support for symlinks (non-native format)
 - ``vers``: SMB protocol version
 - ``soft``: return error if the server does not responds (do not hang)
 - ``hard``: opposite of ``soft``: hang until the read/write succeed

Configurations
--------------

.. code-block:: unixconfig
   :caption: /etc/fstab

   XXXX		/				XXXX		relatime								0 1
   XXXX		/boot				XXXX		nodev,nosuid,noexec,noatime						0 2
   XXXX		/boot/efi			vfat		nodev,nosuid,noexec,noatime,fmask=0177,dmask=0077,errors=remount-ro	0 2
   XXXX		/home				XXXX		nodev,nosuid,lazytime							0 2
   XXXX		/var				XXXX		nodev,nosuid,noexec,relatime						0 2
   XXXX		none				swap		sw,discard=once								0 0
   
   proc		/proc				proc		nodev,nosuid,noexec,hidepid=2,gid=${ID of proc group}			0 0
   tmpfs	/tmp				tmpfs		nodev,nosuid,noexec,noatime,size=1g,mode=1777				0 0
   tmpfs	/run				tmpfs		nodev,nosuid,noexec,noatime,size=100m,mode=0755				0 0
   shm		/dev/shm			tmpfs		nodev,nosuid,noexec,noatime						0 0
   efivarfs	/sys/firmware/efi/efivars	efivarfs	ro,nodev,nosuid,noexec							0 0
   tmpfs	/tmp/apt			tmpfs		nodev,nosuid,exec,noatime,size=100m,mode=0750				0 0

EFI partition: FAT32 does not have permissions, so we set default permissions
for all files to be ``700`` for all files with `umask=0077`.

``/tmp``:
 - tmpfs: files in ``/tmp`` should be wiped at boot and small in size
 - ``noexec``: this may cause issue with software trying to store executables
   in ``/tmp``, however executables should rather be stored somewhere else
   like ``/run``.

efivarfs: mount read-only as a safeguard because broken EFI implementation
may `hard-brick`_ when some EFI variables are removed.

.. _hard-brick: https://lwn.net/Articles/674940/

proc
^^^^

:manpage:`proc(5)`: mount with the ``hidepid`` option to hide the process
list from unprivileged users. The ``gid`` option lets users member of a given
group access to the list of process.

Warning this will break login managers. To fix this, create the *proc* group
(see :ref:`su-label`) and add login services to it.

For systemd:

.. code-block:: systemd
   :caption: /etc/systemd/system/systemd-logind.service.d/hidepid.conf

   [Service]
   SupplementaryGroups=proc

For Gentoo: add ``ACCT_USER_POLKITD_GROUPS_ADD="proc"``
to ``/etc/portage/make.conf`` to add the *polkitd* user to the *proc* group.

Other configurations
--------------------

.. code-block:: unixconfig
   :caption: /etc/fstab

   //XXX/XXX	/mnt/xxx			cifs		user,rw,nodev,nosuid,exec,uid=xxxx,gid=xxxx,credentials=/etc/cifs/keys/xxxx-root.cifs,vers=3,mfsymlinks,soft,file_mode=0750,dir_mode=0750	0 0
