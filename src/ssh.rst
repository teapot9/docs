SSH
===

Close innactive sessions
------------------------

.. code-block:: unixconfig
   :caption: /etc/ssh/sshd_config

   ClientAliveInterval 600
   ClientAliveCountMax 3
   LoginGraceTime 10

Harden SSH
----------

.. code-block:: unixconfig
   :caption: /etc/ssh/sshd_config

   PermitUserEnvironment no
   AllowAgentForwarding no
   AllowTcpForwarding no
   PermitTunnel no

Harden authentication
---------------------

.. code-block:: unixconfig
   :caption: /etc/ssh/sshd_config

   PermitRootLogin no
   PermitEmptyPasswords no
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   KerberosAuthentication no
   GSSAPIAuthentication no

Harden for servers
------------------

.. code-block:: unixconfig
   :caption: /etc/ssh/sshd_config

   X11Forwarding no

Restrict authorized keys management to root
-------------------------------------------

``~/.ssh/authorized_keys`` is usually managed and owned by the user, this
allow the user to add public keys to authenticate with.
However, this also allow any process running as the user to edit this file.
This configuration change the location of the "authorized keys" file
and restrict write to root.
This also restricts read to root and the user itself.

Create the authorized keys directory:

.. code-block:: console

   # mkdir /etc/ssh/authorized_keys
   # chmod 751 /etc/ssh/authorized_keys

Add "foo" user authorized keys:

.. code-block:: console

   # touch /etc/ssh/authorized_keys/foo
   # chown root:foo /etc/ssh/authorized_keys/foo
   # chmod 640 /etc/ssh/authorized_keys/foo

Update ``sshd_config``:

.. code-block:: unixconfig
   :caption: /etc/ssh/sshd_config

   AuthorizedKeysFile /etc/ssh/authorized_keys/%u

Dropbear
--------

OpenRC:

.. code-block:: unixconfig
   :caption: /etc/conf.d/dropbear

   DROPBEAR_OPTS="-w -s -T 3 -j -k"

Command-line:
 - ``-w``: disable root login
 - ``-s``: disable password login
 - ``-T 3``: maximum authentication tries
 - ``-j -k``: disable local and remote port forwarding

Restrict authorized keys management to root
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With Dropbear, you cannot customize the path of the ``authorized_keys`` file.
However, you can make the file writeable only by root by making it
immutable.

.. code-block:: console
   :caption: Make authorized_keys immutable

   # chattr +i /home/*/.ssh/authorized_keys

You can remove the immutable attribute with the ``chattr -i`` command.
