import paramiko

def main():
    command = "echo Hello World!"
    host = "16.16.8.216"
    username = "bandit0"
    password = "bandit0"
    port = 2220

    ssh_client = paramiko.client.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, username=username, password=password, port=port)
    stdin, stdout, stderr = ssh_client.exec_command(command)
    print(stdout.read().decode())
    ssh_client.close()

def execute_command(client, command):

    channel = client.get_transport().open_session()

    channel.exec_command(command)

    output = channel.recv(1024).decode('utf-8')
    return output

def main2():

    print("Estaremos implementando el ejercicio de bandit3 --> bandit4")
    print(linea())
    print("La consigna es la siguiente:")
    print("- La contraseña del siguiente nivel esta almacenada en una archivo oculto dentro del directorio 'inhere'")
    print("Para esto haremos la conexion atraves de la libreria paramiko de python")
    print("Nos conectaremos atraves del protocolo SSH, para esto requerimos el nombre del host, el puerto y el usuario, ademas de la contraseña")
    print(linea())
    
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host_name = "bandit.labs.overthewire.org"
    port = 2220
    user_name = "bandit3"
    password = "aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG"

    client.connect(host_name, port=port, username=user_name, password=password)

    print(linea())
    print("Tras haber conectado, seguiremos las instrucciones")
    print("Veremos si existe el directorio inhere")

    print(linea())
    print(execute_command(client, 'ls'))
    print(linea())

    print("Luego iremos a ese directorio")
    execute_command(client, 'cd inhere')
    print(linea())

    print("Tras esto, veremos si hay algun archivo dentro del directorio:")
    print("Ejecutaremos ls")
    print(linea())
    print(execute_command(client, 'ls'))
    print(linea())

    print("Como vemos, no aparece nada, eso es por que el archivo esta oculto, eso quiere decir que tendremos que hacerle especificaciones a ls")
    print("Usaremos el comando 'ls -a', la a siendo de absoluto, lo cual nos permitira acceder a los archivos ocultos")
    print(linea())

    print(execute_command(client, 'ls -a'))
    print(linea())

    print("Como vemos, hay un archivo que se llama .hidden, accederemos a ese archivo con el comando cat .hidden")
    print(linea())
    print(execute_command(client, 'cat .hidden'))
    print(linea())

    print("Asi obtendremos la contraseña para el siguiente nivel")



    

def linea(n=1):
    result = ""
    for i in range(n):
        result+= "------------------------\n"
    return result


if __name__=='__main__':
    main2()
