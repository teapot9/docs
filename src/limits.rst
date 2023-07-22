System limits
=============

Limits are configured system-wide and apply to all non-root users.
Limits can be changed with the :manpage:`ulimit(1p)` command.

Soft limit: default limit value.
Hard limit: maximum value that can be set with ulimit.

Limits
------

 - ``nproc``: maximum number of process a user can start.
   Setting this can protect your system from fork bombs.
 - ``nofile``: maximum number of open file descriptors for a user.
 - ``memlock``: maximum locked-in-memory address space
   (this prevent from being swapped for instance).
 - ``nice``: minimum nice value (max priority) allowed to be set [-20, 19].
 - ``core``: limit size of core dumps, can be disabled with 0.

Configuration
-------------

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
