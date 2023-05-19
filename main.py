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

if __name__=='__main__':
    main()