Troubleshooting
===============

fork: retry: Resource temporarily unavailable
---------------------------------------------

nproc
^^^^^

System start crashing and shells are telling you
``fork: retry: Resource temporarily unavailable``.

This may be caused by a rogue process starting lots of threads or children,
making you reach your process number limit.
You can get a list of process and threads with ``ps -eFT``.
If you can't get a shell, try switching to another TTY, or remoting with SSH.

This limit is configured as ``nproc`` in :doc:`limits`.

Spice: X11 does not resize screen
---------------------------------

Create the script to resize and add udev rule to run it when
the window is resized
(source: `superuser <https://superuser.com/a/1211261>`_).

.. code-block:: sh
   :caption: /usr/local/bin/x-resize

   #!/bin/sh
   desktopuser=$(/bin/ps -ef | /bin/grep -oP '^\w+ (?=.*vdagent( |$))') || exit 0
   export DISPLAY=:0
   export XAUTHORITY=$(eval echo "~$desktopuser")/.Xauthority
   xrandr --output $(xrandr | awk '/ connected/{print $1; exit; }') --auto

.. code-block::
   :caption: /etc/udev/rules.d/50-x-resize.rules

   ACTION=="change", KERNEL=="card0", SUBSYSTEM=="drm", RUN+="/usr/local/bin/x-resize"

.. code-block:: console
   :caption: Set permissions

   # chmod 755 /usr/local/bin/x-resize
   # chmod 644 /etc/udev/rules.d/50-x-resize.rules
