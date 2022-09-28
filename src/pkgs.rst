Packages
========

Essential tools
---------------

.. list-table:: Essential tools
   :header-rows: 1
   
   * - Package
     - Gentoo
     - Debian / Ubuntu
     - Alpine
   * - GnuPG
     - | app-crypt/gnupg
     - | gnupg
     - | gnupg
   * - Text editor
     - | app-editors/vim
       | app-editors/nano
     - | vim
       | nano
     - | vim
       | nano
   * - Busybox
     - | sys-apps/busybox
     - | busybox
     - | busybox
   * - Shell
     - | app-shells/dash
       | app-shells/bash
     - | dash
       | bash
     - | dash
       | bash
   * - Terminal
     - | app-misc/screen
       | app-misc/tmux
     - | screen
       | tmux
     - | screen
       | tmux
   * - SSH
     - | virtual/ssh
       | net-misc/openssh
       | net-misc/dropbear
     - | ssh
       | openssh-client
       | openssh-server
       | dropbear
     - | openssh
       | dropbear
       | dropbear-ssh
   * - rsync
     - | net-misc/rsync
     - | rsync
     - | rsync
   * - Antivirus
     - | app-antivirus/clamav
       | app-antivirus/fangfrisch
     - | clamav
       | clamav-daemon
       | clamav-unofficial-sigs
     - | clamav
   * - Archives
     - | app-arch/p7zip
     - | p7zip-full
       | p7zip-rar
     - | p7zip
   * - Monitoring
     - | sys-process/htop
     - | htop
     - | htop

Hardware
--------

.. list-table:: Hardware
   :header-rows: 1
   
   * - Package
     - Gentoo
     - Debian / Ubuntu
     - Alpine
   * - Firmwares
     - | sys-kernel/linux-firmware
       | sys-firmware/intel-microcode
     - | linux-firmware
       | amd64-microcode
       | intel-microcode
     - | linux-firmware
       | amd-ucode
       | intel-unicode
   * - Drivers
     - | x11-drivers/nvidia-drivers
     - | nvidia-driver
       | *ubuntu: use* ``update-manager`` *GUI*
     - | 
   * - WiFi
     - | net-wireless/wireless-regdb
     - | 
     - | 
   * - Virtual machine
     - | app-emulation/qemu-guest-agent
       | app-emulation/spice-vdagent
     - | qemu-guest-agent
       | spice-vdagent
     - | qemu-guest-agent
       | spice-vdagent
   * - Partitions
     - | sys-block/parted
     - | parted
     - | parted

Admin tools
-----------

.. list-table:: Admin tools
   :header-rows: 1
   
   * - Package
     - Gentoo
     - Debian / Ubuntu
     - Alpine
   * - Kernel modules
     - | sys-apps/kmod
     - | kmod
     - | kmod
   * - PCI
     - | sys-apps/pciutils
     - | pciutils
     - | pciutils
   * - PCMCIA
     - | sys-apps/pcmciautils
     - | pcmciautils
     - | pcmciautils
   * - USB
     - | sys-apps/usbutils
     - | usbutils
     - | usbutils
   * - SCSI
     - | sys-fs/lsscsi
     - | lsscsi
     - | lsscsi
   * - Superuser
     - | app-admin/doas
       | app-admin/sudo
     - | doas
       | sudo
     - | doas
       | sudo
   * - Restart services
     - | app-admin/restart-services
       | app-admin/needrestart
     - | needrestart
     - | restart-services

Packages notes
--------------

vim
^^^

Disable mouse by default:

.. code-block::
   :caption: /etc/vim/vimrc.local

   set mouse=
   set ttymouse=
