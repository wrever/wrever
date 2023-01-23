import http.client

Host = input("ingrese una direccion ip>>> ")
Port = input("ingrese un puerto>>> ")
Path = input("Ingrese un path>>> ")
conexion = http.client.HTTPConnection(Host, Port)
print("[+] Conexion Exitosa")
conexion.request("GET", Path)
print("                               ")
respuesta = conexion.getresponse()
print("Status: {} y reason: {}".format(respuesta.status, respuesta.reason))

print("                                    ")
print("[-] Conexion Cerrada Correctamente")
conexion.close()