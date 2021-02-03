import os
import pathlib
import time


class ControllerDomain:
    
    def __init__(self, domain = "safehome.local", host = "linux", hostname = "linux", ip="10.10.10.10", gateway="10.10.10.1", interface="ens33"):
        
        self.domain = domain
        self.host = host
        self.hostname = hostname
        self.ip = ip
        self.gateway = gateway
        self.interface = interface 

    ## Metodos Getters
    def set_domain(self, domain):
        self.domain = domain
    
    def set_g4(self, g4):
        self.gateway = g4

    def set_inter(self, inter):
        self.inter = inter


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

    def get_g4(self):
        g4 = self.gateway
        return g4

    def get_inter(self):
        inter = self.interface
        return inter

    def get_host(self):
        host = self.host
        return host

    def get_ip(self):
        ip = self.ip
        return ip

    # Acciones

    def file_hostname(self):
        hostname = self.hostname
        domain = self.domain
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/conf/hostname", "w")
        file.write(f"{hostname}\n")
        file.close()
        file2 = open(f"{ruta}/conf/domain", "w")
        file2.write(f"{domain}\n")
        file2.close()
        return "Archivo Hostname Generado"

    def file_hosts(self):
        hostname = self.hostname
        domain = self.domain
        ip = self.ip
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/conf/hosts", "w")
        file.write(f"""
127.0.0.1   localhost
127.0.0.1   {hostname}.{domain} {hostname}
{ip}   {hostname}.{domain} {hostname}
        \n""")
        file.close()
        return "Archivo Hosts Generado"

    def file_resolv(self):
        domain = self.domain
        ip = self.ip
        resolv = f"""
domain {domain}
nameserver 127.0.0.1
        \n"""
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/conf/resolv.conf", "w")
        file.write(resolv)
        file.close()
        return "Archivo Resolv Generado"
    
    def network(self):
        ip = self.ip
        g4 = self.gateway
        inter = self.interface
        net = f"""
network:
    version: 2
    renderer: networkd
    ethernets:
        {inter}:
            addresses:
                - {ip}/24
            gateway4: {g4}
            nameservers:
                addresses: [8.8.8.8, 8.8.4.4]
        \n"""
        ruta = str(pathlib.Path().absolute())
        file = open(f"{ruta}/conf/config.yaml", "w")
        file.write(net)
        file.close()
        return "Archivo de RED Generado"


    def probe(self):
        domain = self.domain
        hostname = self.hostname
        s_ldap = os.system(f'host -t SRV _ldap._tcp.{domain}')
        time.sleep(15)
        s_krb5 = os.system(f'host -t SRV _kerberos._udp.{domain}')
        time.sleep(15)
        s_a = os.system(f'host -t A {hostname}.{domain}')
        time.sleep(15)
        test = os.system(f'sudo testparm')
        return [s_ldap,s_krb5,s_a, test]

    def install(self):
        ruta = str(pathlib.Path().absolute())
        script = os.system(f'chmod +x {ruta}/src/install.sh && {ruta}/src/install.sh')