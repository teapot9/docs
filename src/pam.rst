PAM
===

Linux PAM (Pluggable Authentication Modules) manages authentication.

Login
-----

Login configuration can be found in ``/etc/login.defs``. This lets you configure
password hashing and expiration. This is the config file of the shadow package.

 - Default umask value: ``UMASK``, see :doc:`shell`.
 - Expire passwords: ``PASS_MIN_DAYS`` and ``PASS_WARN_AGE``.
 - Configure the number of rounds for password hashing:
   ``SHA_CRYPT_MIN_ROUNDS``, ``SHA_CRYPT_MAX_ROUNDS``.

Configuration
^^^^^^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/login.defs

   UMASK 027
   PASS_MIN_DAYS 1
   PASS_MAX_DAYS 365
   SHA_CRYPT_MIN_ROUNDS 50000
   SHA_CRYPT_MAX_ROUNDS 500000
   FAIL_DELAY 3

.. code-block:: console
   :caption: Setting password expiration

   # chage --maxdays 365 root

Environment
-----------

Environment variables defined in ``/etc/environment`` will always
be loaded. It is loaded by :doc:`pam` after authenticating.

System-wide useful environment variables:

.. code-block:: unixconfig
   :caption: /etc/environment

   PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/bin"
   EDITOR="vi"
   VISUAL="vim"
   PAGER="less"

System limits
-------------

Limits are configured system-wide and apply to all non-root users.
Limits can be changed with the :manpage:`ulimit(1p)` command.

Soft limit: default limit value.
Hard limit: maximum value that can be set with ulimit.

 - ``nproc``: maximum number of process a user can start.
   Setting this can protect your system from fork bombs.
 - ``nofile``: maximum number of open file descriptors for a user.
 - ``memlock``: maximum locked-in-memory address space
   (this prevent from being swapped for instance).
 - ``nice``: minimum nice value (max priority) allowed to be set [-20, 19].
 - ``core``: limit size of core dumps, can be disabled with 0.

Configuration
^^^^^^^^^^^^^

.. code-block:: unixconfig
   :caption: /etc/security/limits.conf

   *		soft	nproc		2000
   *		hard	nproc		4000
   *		soft	nofile		4096
   *		hard	nofile		524288
   *		soft	memlock		128
   *		hard	memlock		256
   *		-	core		0
   @wheel	-	nice		-5
   @kernel	-	nice		-5

mktemp
------

Creates a private temporary directory for the user, and sets TMP and
TMPDIR accordingly.

Installation:

 - Gentoo: ``sys-auth/pambase``: ``mktemp`` useflag
 - Debian, Ubuntu: ``libpam-tmpdir`` package

Secure TTY
----------

The :manpage:`securetty(5)` file defines which terminals on which root
is allowed to login.

.. code-block::
   :caption: /etc/securetty

   console
   tty1
   tty2
   tty3
   tty4
   tty5
   tty6
   tty7
   tty8
   tty9
   tty10
   tty11
   ttyS0
   ttyS1

To enable it, you need to enable the :manpage:`pam_securetty(8)` module
by editing ``/etc/pam.d/login``.

.. code-block::
   :caption: /etc/pam.d/login

   auth		required	pam_securetty.so

Wheel
-----

To restrict the use of :manpage:`su(1)` to users in the *wheel* group,
you can enable the :manpage:`pam_wheel(8)` module.

.. code-block::
   :caption: /etc/pam.d/su and /etc/pam.d/su-l

   auth		required	pam_wheel.so

Login access control
--------------------

The ``/etc/security/access.conf`` restricts where users can login from
(network, local TTY ...).
PAM will check this file on each login and use the first matching rule.

For instance ``+ : root : LOCAL`` will allow root to login locally.
And ``+ : (wheel) : LOCAL 192.168.1.0/24`` will allow members of the
*wheel* group to login locally and from the network *192.168.1.0/24*.
Finally, ``- : ALL : ALL`` will deny login from anyone from anywhere.

.. code-block::
   :caption: /etc/security/access.conf

   # Allow root from LOCAL only
   + : root : LOCAL
   - : root : ALL
   
   # Allow sync from LOCAL
   + : sync : LOCAL
   
   # Allow wheel group from LOCAL and trusted networks
   + : (wheel) : LOCAL 172.16.0.0/16
   - : (wheel) : ALL
   
   # Allow users from anywhere
   + : (users) : ALL
   
   # Block everything by default
   - : ALL : ALL
