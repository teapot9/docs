doas / sudo
===========

Configure root password: ``passwd root``.

Create wheel group, add root to it, and create new admin account:

 - Using shadow utils:

   - ``groupadd -r wheel``
   - ``usermod -aG wheel root``
   - ``useradd -c Teapot -G wheel -m -s /bin/sh teapot``

 - Using busybox utils:

   - ``adduser -g teapot -s /bin/sh teapot``
   - ``addgroup -S wheel root``
   - ``addgroup -S wheel teapot``

doas
----

.. code-block::
   :caption: /etc/doas.conf

   permit persist setenv { TMOUT=1800 PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" } :wheel

sudo
----

.. code-block::
   :caption: /etc/sudoers

   Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
   Defaults	env_keep+="TMOUT"
   %wheel  ALL=(ALL:ALL) ALL

Both of these configurations hardcode the PATH environment variable
and let users from ``wheel`` group elevates their privileges.
