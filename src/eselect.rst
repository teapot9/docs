Default applications
====================

.. list-table:: Essential tools
   :header-rows: 1
   
   * - Application
     - eselect
     - update-alternatives
   * - Editor
     - | editor
       | visual
     - | editor
   * - Java
     - java-vm
     - java
   * - Locale
     - locale
     -
   * - Pager
     - pager
     - pager
   * - sh
     - sh
     -
   * - vi
     - vi
     - | rvim
       | vi
       | vim
   * - Compiler
     -
     - | c++
       | cc
   * - Pinentry
     - pinentry
     - | pinentry
       | pinentry-x11
   * - Browser
     -
     - x-www-browser

Add custom executables with update-alternatives:

.. code-block:: console
   :caption: Add custom editor and visual

   # update-alternatives --install /usr/bin/editor editor /usr/bin/vi 100
   # update-alternatives --install /usr/bin/visual visual /usr/bin/vim 100
