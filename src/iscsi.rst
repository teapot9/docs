iSCSI
=====

Root FS or SWAP on iSCSI
------------------------

Root and swap devices can't fail without blocking or crashing the
entire system.

.. code-block:: unixconfig
   :caption: /etc/iscsi/iscsid.conf

   node.conn[0].timeo.noop_out_interval = 0
   node.conn[0].timeo.noop_out_timeout = 0
   node.session.timeo.replacement_timeout = 86400

Nop-out will fail a device after it has been inaccessible for some time,
setting it to zero disables the feature. Setting replacement timeout to a high
number tell the system to wait a long time for the session to reestablish
itself.
