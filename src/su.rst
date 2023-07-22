doas / sudo
===========

Configure root password: ``passwd root``.

Create wheel group, add root to it, and create new admin account:

 - Using shadow utils:

   - ``groupadd -r wheel``
   - ``usermod -aG wheel root``
   - ``useradd -c Teapot -G wheel -m -s /bin/sh teapot``

 - Using busybox utils:

   - ``adduser -g Teapot -s /bin/sh teapot``
   - ``addgroup -S root wheel``
   - ``addgroup -S teapot wheel``

doas
----

.. code-block::
   :caption: /etc/doas.conf

   permit persist setenv { TMOUT=1800 PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" } :wheel
   permit nopass setenv { TMOUT=1800 PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" } root

Note: if busybox binaries are installed to another directory, you can
add the directory (e.g. ``/usr/libexec/busybox``).

sudo
----

.. code-block::
   :caption: /etc/sudoers

   Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
   Defaults	env_keep+="TMOUT"
   %wheel  ALL=(ALL:ALL) ALL

Both of these configurations hardcode the PATH environment variable
and let users from ``wheel`` group elevates their privileges.
