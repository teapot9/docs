chroot
======

Source: `Gentoo Handbook <https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Copy_DNS_info>`_

We will use ``${CHROOT}`` to refer to the root of the chroot.

Copy DNS configuration
----------------------

.. code-block:: console

   # cp --dereference /etc/resolv.conf "${CHROOT}"/etc/

Mount filesystems
-----------------

.. code-block:: console
   :caption: Mount proc, sys, dev and run

   # mount --types proc /proc "${CHROOT}"/proc
   # mount --rbind /sys "${CHROOT}"/sys
   # mount --make-rslave "${CHROOT}"/sys
   # mount --rbind /dev "${CHROOT}"/dev
   # mount --make-rslave "${CHROOT}"/dev
   # mount --bind /run "${CHROOT}"/run
   # mount --make-slave "${CHROOT}"/run

.. code-block:: console
   :caption: Mount tmpfs

   # test -L /dev/shm && rm /dev/shm && mkdir /dev/shm
   # mount --types tmpfs --options nosuid,nodev,noexec,mode=1777 shm /dev/shm
   # mount --types tmpfs --options nosuid,nodev,noexec,mode=1777 none "${CHROOT}"/tmp

Chroot
------

.. code-block:: console

   # chroot "${CHROOT}" /bin/sh -l
   # . /etc/profile
   # export PS1="(chroot) ${PS1}"

If you only mounted rootfs, you can mount other filesystems
from fstab with ``mount -a``.
