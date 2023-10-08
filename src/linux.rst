Linux kernel
============

Kernel cmdline
--------------

Security
^^^^^^^^

 - ``lockdown=confidentiality`` (see :manpage:`kernel_lockdown(7)`):
   add security restrictions, most notably
   blocks ``/dev/*mem`` and similar special files
 - ``mitigations=auto``
 - ``page_alloc.shuffle=1``
 - ``iommu=force``
 - ``init_on_alloc=1``: zero memory on alloc
 - ``init_on_free=1``: zero memory on free
 - ``debugfs=no-mount``
 - ``randomize_kstack_offset=1``

Hardenning
^^^^^^^^^^

 - ``loadpin.enforce=1``: when the first kernel module is loaded, only load
   other module from the same filesystem; this will probably cause issues if
   the first module is loaded from initramfs
 - ``slab_nomerge``: may have performance impact on memory management

Zswap
^^^^^

`Zswap <https://www.kernel.org/doc/html/latest/admin-guide/mm/zswap.html>`_
is a compressed cache for swap.

 - ``zswap.enabled=1``: enable zswap
 - ``zswap.compressor=zstd``: select compression algorithm (lzo, lz4, lz4hc,
   deflate, ...)

To check the current state of Zswap: ``grep '' /sys/module/zswap/parameters/*``.

Bootloader
----------

GRUB
^^^^

.. code-block:: unixconfig
   :caption: /etc/default/grub

   GRUB_TIMEOUT=1
   GRUB_DISABLE_OS_PROBER=true

``GRUB_TIMEOUT`` will show the GRUB menu for just 1 second.
This should be enough to react when you need to change settings,
but will not take forever to boot when you don't.
``GRUB_DISABLE_OS_PROBER`` will disable the use of ``os-prober``,
keep it enabled if you have dual boot.

Update grub config (depending on your OS):
 - ``update-grub``
 - ``grub-mkconfig -o /boot/grub/grub.cfg``

Kernel cmdline
~~~~~~~~~~~~~~

There are two variables containing kernel cmdline in GRUB:
 - ``GRUB_CMDLINE_LINUX``: will always be used
 - ``GRUB_CMDLINE_LINUX_DEFAULT``: will not be used when booting in recovery

File permissions
^^^^^^^^^^^^^^^^

You may want to prevent unprivileged read to ``/boot``:
``chmod 750 /boot``.

Note that ``dpkg`` may reset the permissions, to make it persistent, use:
``dpkg-statoverride --add root root 0750 /boot``.
