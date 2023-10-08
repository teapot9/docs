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
   * - Mail transfert agent
     - | mail-mta/msmtp[mta]
     - | msmtp
       | msmtp-mta
     - | msmtp
   * - Mail command
     - | virtual/mailx (virtual)
       | net-mail/mailutils[clients]
       | mail-client/mailx
     - | mailx (virtual)
       | mailutils
       | bsd-mailx
     - | mailx
       | mailutils

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
   * - Firmware update
     - | sys-apps/fwupd
     - | fwupd
     - | fwupd
       | fwupd-openrc
       | fwupd-plugin-all
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
   * - USB whitelisting
     - | sys-apps/usbguard
     - | usbguard
     - | usbguard
       | usbguard-openrc

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

.. code-block:: vim
   :caption: /etc/vim/vimrc.local

   " Source the defaults vim file
   if ! exists('skip_defaults_vim')
   	source $VIMRUNTIME/defaults.vim
   endif
   " Avoid loading the defaults twice
   let g:skip_defaults_vim = 1
   
   " Disable mouse by default
   set mouse=
   "set ttymouse=


.. code-block:: vim
   :caption: /etc/vim/vimrc.local

   " Enable using CTRL+left and CTRL+right to move backward and forward
   map <Esc>[1;5D <C-Left>
   cmap <Esc>[1;5D <C-Left>
   imap <Esc>[1;5D <C-Left>
   map <Esc>[1;5C <C-Right>
   cmap <Esc>[1;5C <C-Right>
   imap <Esc>[1;5C <C-Right>

USBGuard
^^^^^^^^

Generate a ruleset with ``usbguard generate-policy``.

.. code-block:: unixconfig
   :caption: /etc/usbguard/usbguard-daemon.conf

   # Block unknown USB devices
   ImplicitPolicyTarget=block
   # Apply policy to devices present when the daemon starts
   PresentDevicePolicy=apply-policy
   # Keep controllers that are present whent he daemon starts
   PresentControllerPolicy=keep
   # Apply policy to new devices
   InsertedDevicePolicy=apply-policy
   # Prevent abuse against the usbguard daemon
   RestoreControllerDeviceState=false
   # Allow root to edit config through CLI
   IPCAllowedUsers=root
   # Allow members of the plugdev group to edit config through CLI
   IPCAllowedGroups=plugdev

Gnome integration
~~~~~~~~~~~~~~~~~

To integrate with Gnome, you can create a polkit file to allow members of the
plugdev group to talk with USBGuard.
Make sure ``/etc/polkit-1/rules.d`` exists with ``0700`` permissions.

.. code-block:: javascript
   :caption: /etc/polkit-1/rules.d/50-usbguard.rules

   // /etc/polkit-1/rules.d/50-usbguard.rules
   // vim: ft=javascript ts=4 sw=4 et
   // Allow users in wheel group to communicate with USBGuard
   polkit.addRule(function(action, subject) {
       if (
           (
               action.id == "org.usbguard.Policy1.listRules"
               || action.id == "org.usbguard.Policy1.appendRule"
               || action.id == "org.usbguard.Policy1.removeRule"
               || action.id == "org.usbguard.Devices1.applyDevicePolicy"
               || action.id == "org.usbguard.Devices1.listDevices"
               || action.id == "org.usbguard1.getParameter"
               || action.id == "org.usbguard1.setParameter"
           )
           && subject.active == true
           && subject.local == true
           && subject.isInGroup("plugdev")
       ) {
           return polkit.Result.YES;
       }
   });

.. code-block:: console
   :caption: Turn on and block devices by default

   $ gsettings set org.gnome.desktop.privacy usb-protection true
   $ gsettings set org.gnome.desktop.privacy usb-protection-level always

msmtp
-----

.. code-block:: unixconfig
   :caption: /etc/msmtprc

   # Default configuration
   defaults
   auth			on
   tls			on
   tls_starttls		off
   tls_trust_file	system
   syslog		LOG_MAIL
   aliases		/etc/aliases
   domain		%C

.. code-block:: unixconfig
   :caption: ~/.msmtprc

   account		gmail
   host			smtp.gmail.com
   port			465
   from			username+tag@gmail.com
   user			username
   password		password
   account default:	gmail

.. code-block:: unixconfig
   :caption: /etc/mail.rc

   set ask askcc append dot save crt
   ignore Received Message-Id Resent-Message-Id Status Mail-From Return-Path Via Delivered-To
   set mta=/usr/bin/msmtp

.. code-block:: unixconfig
   :caption: /etc/aliases or /etc/mail/aliases

   root:	yourmail@example.com
   operator:	yourmail@example.com
   # trap decode to catch security attacks
   decode:	/dev/null

.. code-block:: console
   :caption: Alpine fix sendmail

   # printf '#!/bin/sh\nln -sf ../bin/msmtp /usr/sbin/sendmail\n' >/etc/local.d/sendmail.start
   # chmod 751 /etc/local.d/sendmail.start
   # /etc/local.d/sendmail.start

Test (as root): ``echo something | mail -s test yourmail@example.com``
