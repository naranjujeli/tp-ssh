import paramiko

def execute_command(client, command):

    channel = client.get_transport().open_session()

    channel.exec_command(command)

    output = channel.recv(1024).decode('utf-8')
    return output

def linea(n=1):
    result = "------------------------"
    for i in range(n-1):
        result+= "------------------------\n"
    return result

def clear_prompt():
    
    import os
    if os.environ == "cmd":
        os.system('cls')
    else:
        os.system('clear')
        
def wait_clear():
    wait()
    clear_prompt()

def wait():
    input(":")

def bold(string):
    bold = "\033[1m"
    white = "\033[0m"
    return bold + string + white

def main():

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host_name = "bandit.labs.overthewire.org"
    port = 2220
    user_name = "bandit3"
    password = "aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG"

    client.connect(host_name, port=port, username=user_name, password=password)

    clear_prompt()

    print(f"Estaremos implementando el ejercicio de {bold('bandit3 --> bandit4')}")
    print(linea())
    print("La consigna es la siguiente:")
    print(f"- La contraseña del siguiente nivel esta almacenada en un archivo oculto dentro del directorio {bold('inhere')}.")
    print("Para esto haremos la conexion a traves de la libreria 'paramiko' de python.")
    print("Nos conectaremos a traves del protocolo SSH, para esto requerimos el nombre del host, el puerto y el usuario, ademas de la contraseña.")
    print(linea())

    wait_clear()

    print("Tras habernos conectado, seguiremos las instrucciones.")
    print(f"Veremos si existe el directorio 'inhere', con el comando {bold('ls')}.")

    print(linea())
    print("Output:")
    print(execute_command(client, 'ls'))
    print(linea())

    wait_clear()

    print(f"Luego iremos a ese directorio con el comando {bold('cd inhere')}.")
    execute_command(client, 'cd inhere')
    print(linea())

    wait_clear()

    print("Tras esto, veremos si hay algun archivo dentro del directorio:")
    print(f"Ejecutaremos {bold('ls')}.")
    print(linea())
    print(execute_command(client, 'cd inhere; ls'))
    print(linea())

    wait_clear()

    print("Como vemos, no aparece nada, eso es por que el archivo esta oculto, eso quiere decir que tendremos que hacerle especificaciones a ls.")
    print(f"Usaremos el comando {bold('ls -a')}, la a siendo de absoluto, lo cual nos permitira acceder a los archivos ocultos.")
    print(linea())
    print(execute_command(client, 'cd inhere; ls -a'))
    print(linea())

    wait_clear()

    print(f"Como vemos, hay un archivo que se llama '.hidden', accederemos a ese archivo con el comando {bold('cat .hidden')}.")
    print(linea())
    print(execute_command(client, 'cd inhere; cat .hidden'))
    print(linea())

    print("Asi obtendremos la contraseña para el siguiente nivel.")
    wait_clear()




if __name__=='__main__':
    main()
