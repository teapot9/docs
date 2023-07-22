Miscellaneous
=============

This regroup uncategorized configurations.

Code snippets
-------------

Code snippets here may have broken indentation when copy-pasting.
To fix it you can use one of the following sed commands:

.. code-block:: sed
   :caption: Fix with spaces

   s/^     /        /

.. code-block:: sed
   :caption: Fix with tabs

   s/^     /\t/
   s/        /\t/g

Hostname on Alpine
------------------

Alpine's hostname configuration sometimes refuse valid hostnames
(e.g. capital letters).

Edit `/etc/hostname` to change it manually.

Install Alpine without SWAP
---------------------------

By default, Alpine install script will create a SWAP partition on the
system drive. To disable this behavior, export ``SWAP_SIZE=0`` in your
environment.
