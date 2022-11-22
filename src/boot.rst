Bootloader
==========

GRUB
----

.. code-block:: unixconfig
   :caption: /etc/default/grub

   GRUB_TIMEOUT=1
   GRUB_DISABLE_OS_PROBER=true

``GRUB_TIMEOUT`` will show the GRUB menu for just 1 second.
This should be enough to react when you need to change settings,
but will not take forever to boot when you don't.
``GRUB_DISABLE_OS_PROBER`` will disable the use of ``os-prober``,
keep it enabled if you have dual boot.

Update grub config:
 - ``update-grub``
 - ``grub-mkconfig -o /boot/grub/grub.cfg``
