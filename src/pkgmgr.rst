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

Firefox non-snap
~~~~~~~~~~~~~~~~

To install Firefox as a normal deb package, install the Mozilla PPA:

.. code-block:: console

   # snap remove firefox
   # add-apt-repository ppa:mozillateam/ppa

.. code-block:: debcontrol
   :caption: /etc/apt/preferences.d/mozilla

   Package: *
   Pin: release o=LP-PPA-mozillateam
   Pin-Priority: 1024

.. code-block:: unixconfig
   :caption: /etc/apt/apt.conf.d/firefox

   Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";

This also lets you install thunderbird as a deb package.

Auto updates
^^^^^^^^^^^^

.. code-block:: console
   :caption: Enable auto updates for apt

   # apt install unattended-upgrades apt-listchanges
   # systemctl enable unattended-upgrades.service

.. code-block:: unixconfig
   :caption: /etc/apt/apt.conf.d/50unattended-upgrades

   Unattended-Upgrade::Mail "root";

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

Auto updates
^^^^^^^^^^^^

.. code-block:: sh
   :caption: /etc/periodic/daily/update

   #!/bin/sh
   set -eu
   
   _atexit() {
   	_code=$?
   	[ -z "${__atexit_code+x}" ] || return "${__atexit_code}"
   	__atexit_code="${_code}"
   
   	if [ "${__atexit_code}" != 0 ]; then
   		die "unknown error"
   	fi
   
   	return "${__atexit_code}"
   }
   trap _atexit INT TERM EXIT
   
   log() {
   	lvl="$1" || :
   	shift
   	echo "$*" 1>&2 || :
   	echo "<$((24 | lvl))>update: $*" 1>/dev/kmsg || :
   }
   
   die() {
   	log 2 "FATAL: $*" 1>&2
   	kill -TERM 0 || :
   	exit 1
   }
   
   # Sanity checks
   [ "$(id -u)" -eq 0 ] || die "need root privileges"
   command -v apk 1>/dev/null 2>&1 || die "need portage"
   
   # Apk update
   log 6 "updating repositories"
   apk update -q || die "apk: sync failed"
   
   # Test if updates available
   avail="$(apk list -uq)" || die "failed to check for upgrades"
   count="$(printf '%s' "${avail}" | wc -l)"
   if [ "${count}" -eq 0 ]; then
   	log 6 "system is up-to-date"
   	exit 0
   fi
   
   # Log updates
   echo "${avail}" | while read -r pkg; do
   	log 5 "will update: ${pkg}"
   done
   
   # Update and send mail
   {
   	apk upgrade || log 3 "ERROR: failed to upgrade system"
   	if echo "${avail}" | grep -q '^nextcloud-'; then
   		occ upgrade -nv || log 3 "ERROR: failed to upgrade nextcloud"
   	fi
   } 2>&1 | mail \
   	-r '@@FQDN@@ <@@FROM@@>' \
   	-s "[APK] system updated" root

Portage
-------

Auto updates
^^^^^^^^^^^^

.. code-block:: sh
   :caption: /etc/cron.d/daily/update

   #!/bin/sh
   set -eu
   
   _atexit() {
   	_code=$?
   	[ -z "${__atexit_code+x}" ] || return "${__atexit_code}"
   	__atexit_code="${_code}"
   
   	if [ "${__atexit_code}" != 0 ]; then
   		die "unknown error"
   	fi
   
   	return "${__atexit_code}"
   }
   trap _atexit INT TERM EXIT
   
   log() {
   	lvl="$1" || :
   	shift
   	echo "$*" 1>&2 || :
   	echo "<$((24 | lvl))>update: $*" 1>/dev/kmsg || :
   }
   
   die() {
   	log 2 "FATAL: $*" 1>&2
   	kill -TERM 0 || :
   	exit 1
   }
   
   # Sanity checks
   [ "$(id -u)" -eq 0 ] || die "need root privileges"
   command -v emerge 1>/dev/null 2>&1 || die "need portage"
   
   # Emerge sync
   log 6 "updating repositories"
   emerge --quiet --sync || die "emerge: sync failed"
   
   # Test if vulnerability
   ret="$(set +e; glsa-check -tq affected 1>/dev/null 2>&1; echo "$?")"
   if [ "${ret}" = 0 ]; then
   	log 6 "system is not affected"
   	exit 0
   elif [ "${ret}" != 6 ]; then
   	die "glsa-check: unexpected exit code: ${ret}"
   fi
   
   # Log vulnerabilities
   glsa-check -lq affected | while read -r vuln; do
   	log 5 "vulnerability: ${vuln}"
   done
   
   # Send mail
   {
   	glsa-check -dq affected
   	emerge -p @security
   } 2>&1 | mail \
   	-r '@@FQDN@@ <@@FROM@@>' \
   	-s "[GLSA] system is affected" root
