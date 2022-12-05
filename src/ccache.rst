Compilation cache
=================

ccache
------

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
^^^^^^^

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

sccache
-------

Portage
^^^^^^^

Setting up for portage:

.. code-block:: unixconfig
   :caption: /etc/sandbox.d/20sccache

   SANDBOX_WRITE="/var/cache/sccache/"

.. code-block:: unixconfig
   :caption: /etc/portage/make.conf or /etc/portage/package.env

   RUSTC_WRAPPER="/usr/bin/sccache"
   SCCACHE_DIR="/var/cache/sccache"
   SCCACHE_MAX_FRAME_LENGTH="104857600"
   SCCACHE_CACHE_SIZE="10G"

.. code-block:: console
   :caption: Setup cache

   # mkdir /var/cache/sccache
   # chown root:portage /var/cache/sccache
   # chmod 2775 /var/cache/sccache

.. code-block:: diff
   :caption: Don't hash current working directory

   diff --git a/src/compiler/rust.rs b/src/compiler/rust.rs
   index f13da45..060d116 100644
   --- a/src/compiler/rust.rs
   +++ b/src/compiler/rust.rs
   @@ -1421,7 +1421,7 @@ where
                }
            }
            // 8. The cwd of the compile. This will wind up in the rlib.
   -        cwd.hash(&mut HashToDigest { digest: &mut m });
   +        //cwd.hash(&mut HashToDigest { digest: &mut m });
            // Turn arguments into a simple Vec<OsString> to calculate outputs.
            let flat_os_string_arguments: Vec<OsString> = os_string_arguments
                .into_iter()
