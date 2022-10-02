Shell
=====

Shell configuration
-------------------

Reloading a shell: run ``exec bash``.

Change login shell: ``chsh -s /bin/bash USER``.

Load profile from ``*shrc``: add ``. /etc/profile.d/00-default.sh`` to:

 - bash: ``/etc/bash/bashrc`` or ``/etc/bash.bashrc``
 - zsh: ``/etc/zsh/zshrc``

umask
-----

Umask defines the default permission of newly created files and directories.
The format is similar to standard permission, but it is NOT-ed.

For instance:
 - ``022`` creates files with ``766`` permissions,
 - ``027`` creates files with ``760`` permissions.

Profile
-------

Configurations in this file will be loaded when the first shell of a session
is started (when logging in, or by using ``sh -l``).

System-wide hardenning configs:

.. code-block:: sh
   :caption: /etc/profile.d/00-default.sh

   umask 027
   case "$0" in -*)
   	# Only if login shell
   	export TMOUT=1800 2>/dev/null
   	readonly TMOUT 2>/dev/null
   	;;
   esac

System-wide useful configs:

.. code-block:: sh
   :caption: /etc/profile.d/00-default.sh

   alias cp='cp --reflink=auto'
   alias ls='ls --color=auto'
   alias ll='ls -lh'
   alias la='ls -lhaF'
   
   alias pfile='install -m 644 /dev/null'
   alias pdir='install -d -m 755'
   
   export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/bin'

~

 - ``cp --reflink=auto`` will use a copy-on-write (CoW) copy if available.
 - ``pfile`` and ``pdir`` creates file or directories accessible to others,
   this may be useful when umask defaults to 640.

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
