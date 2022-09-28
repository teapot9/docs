Kernel cmdline
==============

Security
--------

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
----------

 - ``loadpin.enforce=1``: when the first kernel module is loaded, only load
   other module from the same filesystem; this will probably cause issues if
   the first module is loaded from initramfs
 - ``slab_nomerge``: may have performance impact on memory management
