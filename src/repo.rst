Package managers
================

APT
---

Backports: packages from newer (or in development) distro version
made available to older releases.

TMPDIR is noexec
^^^^^^^^^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/apt/apt.conf
   
   APT::ExtractTemplates::TempDir "/run/apt";

Manually installed packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The set of manually installed packages in APT is the list of packages
that will be kept even if they have no reverse dependencies.

This list can be viewed with ``apt-mark showmanual``.

You can shrink this set by removing packages that are dependencies
of meta packages.

.. code-block:: console
   :caption: Minimize manually installed packages set

   # apt-mark minimize-manual

Debian
^^^^^^

.. code-block:: sourceslist
   :caption: /etc/apt/sources.list

   deb http://deb.debian.org/debian XXXX main contrib non-free
   deb-src http://deb.debian.org/debian XXXX main contrib non-free
   
   deb http://deb.debian.org/debian-security/ XXXX-security main contrib non-free
   deb-src http://deb.debian.org/debian-security/ XXXX-security main contrib non-free
   
   deb http://deb.debian.org/debian XXXX-updates main contrib non-free
   deb-src http://deb.debian.org/debian XXXX-updates main contrib non-free
   
   deb http://deb.debian.org/debian bullseye-backports main contrib non-free
   deb-src http://deb.debian.org/debian bullseye-backports main contrib non-free

To install packages from backports, run either:
 - ``apt install foo/bullseye-backports``
 - ``apt install -t bullseye-backports foo``

Old-stable-sloppy
~~~~~~~~~~~~~~~~~

Backports from debian testing, generally have the latest
version available.

However:
 - unsupported / unstable;
 - may cause issues when upgrading between stable releases.

Usage: same as backports, except it is ``XXXX-backports-sloppy``.

Ubuntu
^^^^^^

.. code-block:: sourceslist
   :caption: /etc/apt/sources.list

   deb http://fr.archive.ubuntu.com/ubuntu/ XXXX main restricted universe multiverse
   deb http://fr.archive.ubuntu.com/ubuntu/ XXXX-updates main restricted universe multiverse
   deb http://fr.archive.ubuntu.com/ubuntu/ XXXX-backports main restricted universe multiverse
   deb http://security.ubuntu.com/ubuntu XXXX-security main restricted universe multiverse

APK
---

.. code-block:: unixconfig
   :caption: /etc/apk/repositories

   http://dl-cdn.alpinelinux.org/alpine/vXX/main
   http://dl-cdn.alpinelinux.org/alpine/vXX/community

LBU (Alpine local backup)
^^^^^^^^^^^^^^^^^^^^^^^^^

In diskless mode, Alpine run entirely in RAM.
Changes to the filesystem are lost during reboots. Use ``lbu ci`` to
commit changes.

By default, ``lbu`` will save changes made to ``/etc``. To preserve additional
directories, use ``lbu add XXX``.

Configure lbu to keep 3 backups and remove older ones:

.. code-block:: unixconfig
   :caption: /etc/lbu/lbu.conf

   BACKUP_LIMIT=3
