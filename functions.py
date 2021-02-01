## Actions ##
import banners
import time
from clean import limpiar
from controllerdomain import ControllerDomain

# Objecto
dominio = ControllerDomain()

# Menu
def menu():
  while True:
    cd = banners.presentacion()
    print(cd)
    menu = """
    Opciones:
    [1] Instalar Controlador de Dominio
    [2] Administrar Controlador de Dominio
    [3] Salir
    """
    print(menu)
    accion = input("lucho@romer ~$ ")

    if accion == "1":
      limpiar()
      install_dc()

    elif accion == "2":
      limpiar()
      print("\n Administrando")

    elif accion == "3":
      limpiar()
      exit()

## Instalacion
def install_dc():
  count = 0
  while True:
    install = banners.install()
    print(install)

    domainExample = "safehome.local"
    hostnameExample = "linux"
    ipExample = "10.10.10.10"

    if count == 0:
      print(f"""
      Ejemplos:
      Dominio : {domainExample}
      Hostname : {hostnameExample}
      IP : {ipExample}
      """)
    else:
      print(f"""
      Dominio: {dominio.get_domain()}
      Hostname: {dominio.get_hostname()}
      IP : {dominio.get_ip()}
      """)

    acciones = """
      Opciones:
      [1] Configuracion
      [2] Instalar
      [3] Comprobar
      [10] Salir
    """
    print(acciones)
    accion = input("lucho@romer ~$ ")

    if accion == "1":
      domain = input("Introduce tu Dominio: ")
      hostname = input("Introduce tu Hostname: ")
      ip = input("Introduce tu IP: ")
      dominio.set_domain(domain)
      dominio.set_hostname(hostname)
      dominio.set_ip(ip)
      count += 1
      limpiar()

    elif accion == "2":
      dominio.install()
      limpiar()

    elif accion == "3":
      comprobacion = dominio.probe()
      print("Comprobacion con Host LDAP")
      time.sleep(10)
      print(f"{comprobacion[0]}")
      print("Comprobacion con Host Kerberos")
      time.sleep(10)
      print(f"{comprobacion[1]}")
      print("Comprobacion con Host Registros A")
      time.sleep(10)
      print(f"{comprobacion[2]}")
      print("Comprobacion con TestParm")
      time.sleep(10)
      print(f"{comprobacion[3]}")

    elif accion == "10":
      limpiar()
      menu()

    else:
      limpiar()