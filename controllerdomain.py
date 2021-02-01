import os
import pathlib
import banners
import time
from clean import limpiar


class ControllerDomain:
    
    def __init__(self, domain = "safehome.local", host = "linux", hostname = "linux", ip="10.10.10.10"):
        
        self.domain = domain
        self.host = host
        self.hostname = hostname
        self.ip = ip

    ## Metodos Getters
    def set_domain(self, domain):
        self.domain = domain


    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_host(self):
        pass

    def set_ip(self, ip):
        self.ip = ip

    def get_domain(self):
        domain = self.domain
        return domain

    def get_hostname(self):
        hostname = self.hostname
        return hostname

    def get_host(self):
        host = self.host
        return host

    def get_ip(self):
        ip = self.ip
        return ip

    # Acciones

    def file_hostname(self):
        hostname = self.hostname
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/hostname", "w")
        file.write(f"{hostname}")
        file.close()
        return "Archivo Hostname Creado"

    def file_hosts(self):
        hosts = self.host
        hostname = self.hostname
        domain = self.domain
        ip = self.ip
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/hosts", "w")
        file.write(f"""
        127.0.0.1	localhost
        127.0.0.1   {hostname}.{domain} {hostname}
        {ip}	{hostname}.{domain} {hostname}
        """)
        file.close()
        return "Archivo Hosts Creado"

    def file_resolv(self):
        domain = self.domain
        ip = self.ip
        resolv = f"""
        domain {domain}
        nameserver {ip}
        """
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/resolv.conf", "w")
        file.write(resolv)
        file.close()
        return "Archivo Resolv Creado"

    def probe(self):
        domain = self.domain
        hostnameExample = self.hostname
        s_ldap = os.system(f'host -t SRV _ldap._tcp.{domain}')
        time.sleep(15)
        s_krb5 = os.system(f'host -t SRV _kerberos._udp.{domain}')
        time.sleep(15)
        s_a = os.system(f'host -t A {hostname}.{domain}')
        time.sleep(15)
        test = os.system(f'sudo testparm')
        return [s_ldap,s_krb5,s_a, test]

    def install():
        ruta = str(pathlib.Path().absolute())
        script = os.system(f'gnome-terminal -e {ruta}/install.sh')