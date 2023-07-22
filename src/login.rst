Login / shadow
==============

Login configuration can be found in ``/etc/login.defs``. This lets you configure
password hashing and expiration. This is the config file of the shadow package.

Login
-----

 - Default umask value: ``UMASK``, see :doc:`shell`.
 - Expire passwords: ``PASS_MIN_DAYS`` and ``PASS_WARN_AGE``.
 - Configure the number of rounds for password hashing:
   ``SHA_CRYPT_MIN_ROUNDS``, ``SHA_CRYPT_MAX_ROUNDS``.

Configuration
-------------

.. code-block:: unixconfig
   :caption: /etc/login.defs

   UMASK 027
   PASS_MIN_DAYS 1
   PASS_MAX_DAYS 365
   SHA_CRYPT_MIN_ROUNDS 50000
   SHA_CRYPT_MAX_ROUNDS 500000

.. code-block:: console
   :caption: Setting password expiration

   # chage --maxdays 365 root
