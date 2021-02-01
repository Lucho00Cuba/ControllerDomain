#!/bin/bash

# Funciones

function update {
    sudo apt-get update && sudo apt-get upgrade -y && sudo apt autoremove -y
}

function files {
    sudo rm /etc/hostname
    sudo rm /etc/hosts
    sudo cp ~/ControllerDomain/src/hostname /etc/hosts
    sudo cp ~/ControllerDomain/src/hosts /etc/hostname
}

function apps {
    sudo apt-get install samba winbind smbclient ntp -y
}

function kerberos {
    sudo apt-get install krb5-user libpam-krb5 lib-ccreds auth-client-config -y
}

function controller_domain {
    # samba
    sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.old
    sudo samba-tool domain provision --use-rfc2307 --interactive
    sudo samba-tool domain level show
    
    # kerberos
    sudo cp /etc/krb5.conf /etc/krb5.conf.old
    sudo cp /var/lib/samba/private/krb5.conf /etc/
    
    #  services
    sudo systemctl stop smbd nmbd winbind systemd-resolved
    sudo systemctl disable smbd nmbd winbind systemd-resolved
    sudo systemctl unmask samba-ad-dc
    sudo rm /etc/resolv.conf
    sudo cp ~/ControllerDomain/resolv.conf /etc/

    sudo systemctl stop samba-ad-dc
    sudo systemctl start samba-ad-dc
    "sudo systemctl enable samba-ad-dc"
}

# Main

# Permisos
sudo -l
update
files
apps
kerberos
controller_domain