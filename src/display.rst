Desktop environment
===================

Xorg
----

You can harden the system wrapper by disabling root and restricting
login to users on a physical console.

.. code-block::
   :caption: /etc/X11/Xwrapper.config

   allowed_users=console
   needs_root_rights=no
