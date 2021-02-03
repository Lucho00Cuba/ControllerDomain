# Importaciones
import time
from mod import banners
from mod import functions
from mod.controllerdomain import ControllerDomain

# Functions
def menu():
  while True:
    cd = banners.presentacion()
    print(cd)
    menu = """
    Opciones:
    [1] Instalar Controlador de Dominio
    [2] Administrar Controlador de Dominio
    [10] Salir
    """
    print(menu)
    accion = input("lucho@linux ~$ ")

    if accion == "1":
      functions.limpiar()
      install_dc()

    elif accion == "2":
      functions.limpiar()
      print("\n Administrando")

    elif accion == "10":
      functions.limpiar()
      exit()

def install_dc():
  count = 0
  while True:
    install = banners.install()
    print(install)

    domainExample = "safehome.local"
    hostnameExample = "linux"
    ipExample = "10.10.10.10"
    g4Example = "10.10.10.1"
    interExample = "ens33"

    if count == 0:
      print(f"""
      Ejemplos:
      Dominio : {domainExample}
      Hostname : {hostnameExample}
      IP : {ipExample}
      GATEWAY : {g4Example}
      INTERFACE : {interExample}
      """)
    else:
      print(f"""
      Dominio: {dominio.get_domain()}
      Hostname: {dominio.get_hostname()}
      IP : {dominio.get_ip()}
      GATEWAY : {dominio.get_g4()}
      INTERFACE : {dominio.get_inter()}
      """)

    acciones = """
      Opciones:
      [1] Configuracion
      [2] Instalar
      [3] Comprobar
      [10] Salir
    """
    print(acciones)
    accion = input("lucho@linux ~$ ")

    if accion == "1":
      domain = input("Introduce tu Dominio: ")
      hostname = input("Introduce tu Hostname: ")
      ip = input("Introduce tu IP: ")
      g4 = input("Introduce tu Puerta de Enlace: ")
      inter = input("Introduce la Interfaz de Red: ")
      dominio.set_domain(domain)
      dominio.set_hostname(hostname)
      dominio.set_ip(ip)
      dominio.set_g4(g4)
      dominio.set_inter(inter)
      count += 1
      functions.limpiar()

    elif accion == "2":
      functions.limpiar()
      count = 0
      if count == 0:
        while True:
          functions.limpiar()
          banners.warning()
          print("""
          Introducir una contraseña de 8 caracteres para el Administrador
          del Controlador de Dominio sino da error

          Example : MiAdminFull00# 

          Nuestro Captcha :)
          2 + 2 = ?

          Escribir "back" para volver atras !

          """)
          c = input("\nResultado~$ ")

          if c == "4":
            functions.limpiar()
            print("\nPreparando Componentes para instalar...\n")
            hostname = dominio.file_hostname()
            hosts = dominio.file_hosts()
            resolv = dominio.file_resolv()
            net = dominio.network()
            lista = [hostname,hosts,resolv,net]
            for i in lista:
              print(f"[*] {i}")
            time.sleep(5)
            print("\nComenzando la Instalacion\n")
            time.sleep(5)
            dominio.install()
            install_dc()

          elif c == "back":
            functions.limpiar()
            count += 1
            install_dc()

          elif c != "4":
            pass
          else:
            pass

        time.sleep(5)
      #dominio.install()
      functions.limpiar()

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
      functions.limpiar()
      menu()

    else:
      functions.limpiar()


# Objecto
dominio = ControllerDomain()

# Main
menu()

#print("\nSaliendo..\n")