ccache
======

.. code-block::
   :caption: /var/cache/ccache/ccache.conf

   max_size = 10.0G
   compiler_check = %compiler% -dumpmachine; %compiler% -dumpversion
   umask = 0007
   hash_dir = false
   cache_dir_levels = 3

..

 - ``compiler_check``: don't drop cache when rebuild the compiler.
 - ``hash_dir``: don't drop cache when build a new package version
   (don't include file path in the hash).

Portage
-------

Setting up for portage: add ``FEATURES=ccache`` to ``make.conf`` or
to ``/etc/portage/package.env``.

.. code-block:: console
   :caption: Setup cache

   # mkdir /var/cache/ccache
   # chown root:portage /var/cache/ccache
   # chmod 2775 /var/cache/ccache
   # touch /var/cache/ccache/ccache.conf
   # chown root:portage /var/cache/ccache/ccache.conf
   # chmod 644 /var/cache/ccache/ccache.conf
   # "$VISUAL" /var/cache/ccache/ccache.conf
