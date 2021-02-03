#!/bin/bash

# Main

echo " "
echo "#################################"
echo "########## HOSTNAME #############"
echo "#################################"
echo " "
hostname=$(cat ~/ControllerDomain/conf/hostname)
sudo hostnamectl set-hostname $hostname
echo " "
echo "#################################"
echo "############ HOSTS ##############"
echo "#################################"
echo " "
sudo mv /etc/hosts /etc/hosts.old
sudo cp ~/ControllerDomain/conf/hosts /etc/hosts
echo " "
echo "#################################"
echo "########## NETWORKING ###########"
echo "#################################"
echo " "
sudo rm /etc/netplan/*
sudo mv ~/ControllerDomain/conf/config.yaml /etc/netplan/config.yaml
sudo netplan apply
echo " "
echo "#################################"
echo "######### REPOSITORIOS ##########"
echo "#################################"
echo " "
curl https://gist.githubusercontent.com/ishad0w/788555191c7037e249a439542c53e170/raw/3822ba49241e6fd851ca1c1cbcc4d7e87382f484/sources.list >> server.list
sudo mv server.list /etc/apt/sources.list.d/server.list
sudo apt-get update && sudo apt-get upgrade -y
echo " "
echo "#################################"
echo "############ SERVICES ###########"
echo "#################################"
echo " "
sudo apt-get install ntp samba winbind smbclient -y
echo " "
echo "#################################"
echo "########### KERBEROS #############"
echo "#################################"
echo " "
wget http://archive.ubuntu.com/ubuntu/pool/universe/a/auth-client-config/auth-client-config_0.9ubuntu1_all.deb
sudo apt install -f ./auth-client-config_0.9ubuntu1_all.deb -y && sudo apt-get install krb5-user libpam-krb5 libpam-ccreds -y
sudo rm ~/ControllerDomain/auth-client-config_0.9ubuntu1_all.deb
echo " "
echo "#################################"
echo "########### DOMAIN #############"
echo "#################################"
echo " "
sudo mv /etc/samba/smb.conf /etc/samba/smb.old
sudo samba-tool domain provision --use-rfc2307 --interactive
echo " "
echo "#################################"
echo "########### SAMBA #############"
echo "#################################"
echo " "
sudo samba-tool domain level show
echo " "
echo "#################################"
echo "######## KERBEROS-CONF ##########"
echo "#################################"
echo " "
sudo cp /etc/krb5.conf /etc/krb5.old
sudo cp /var/lib/samba/private/krb5.conf /etc/krb5.conf
sudo systemctl stop smbd nmbd winbind systemd-resolved
sudo systemctl disable smbd nmbd winbind systemd-resolved
sudo systemctl unmask samba-ad-dc
echo " "
echo "#################################"
echo "########### RESOLV #############"
echo "#################################"
echo " "
sudo mv /etc/resolv.conf /etc/resolv.conf.old
sudo cp ~/ControllerDomain/conf/resolv.conf /etc/resolv.conf
echo " "
echo "#################################"
echo "########### TESTING #############"
echo "#################################"
echo " "
sudo systemctl stop samba-ad-dc
sudo systemctl start samba-ad-dc
sudo systemctl enable samba-ad-dc
# Probe
domain=$(cat ~/ControllerDomain/conf/domain)
host -t SRV _ldap._tcp.$domain
host -t SRV _kerberos._udp.$domain
host -t A $hostname.$domain
sudo testparm
# Clean
sudo rm ~/ControllerDomain/conf/*


# Inactivo
function unistall {
    sudo hostnamectl set-hostname $HOSTNAME
    sudo nano /etc/hosts
    Red IP Fija
    REPOS Server >> https://gist.github.com/ishad0w/788555191c7037e249a439542c53e170
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install ntp samba winbind smbclient -y
    wget http://archive.ubuntu.com/ubuntu/pool/universe/a/auth-client-config/auth-client-config_0.9ubuntu1_all.deb
    sudo apt install -f ./auth-client-config_0.9ubuntu1_all.deb && sudo apt-get install krb5-user libpam-krb5 libpam-ccreds
    sudo mv /etc/samba/smb.conf/etc/samba/smb.old
    sudo samba-tool domain provision--use-rfc2307 --interactive
    sudo samba-tool domain level show
    sudo cp /etc/krb5.conf /etc/krb5.old
    sudo cp /var/lib/samba/private/krb5.conf /etc/
    sudo systemctl stop smbd nmbd winbind systemd-resolved
    sudo systemctl disable smbd nmbd winbind systemd-resolved
    sudo systemctl unmask samba-ad-dc
    sudo rm /etc/resolv.conf
    sudo nano /etc/resolv.conf >> domain $DOMAIN, nameserver 127.0.0.1
    sudo systemctl stop samba-ad-dc
    sudo systemctl start samba-ad-dc
    sudo systemctl enable samba-ad-dc
}
