Bootloader
==========

GRUB
----

.. code-block:: unixconfig
   :caption: /etc/default/grub

   GRUB_TIMEOUT=1

This will show the GRUB menu for just 1 second.
This should be enough to react when you need to change settings,
but will not take forever to boot when you don't.
