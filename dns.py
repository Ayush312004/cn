import socket

def main():
    print("1. Enter Host Name\n2. Enter IP address")
    choice = int(input("Choice = "))

    if choice == 1:
        host = input("\nEnter host name: ")
        try:
            address = socket.gethostbyname(host)
            print("IP address:", address)
            print("Host name:", host)
            print("Host name and IP address:", host + "/" + address)
        except socket.gaierror:
            print("Could not find host:", host)

    elif choice == 2:
        ip = input("\nEnter IP address: ")
        try:
            host_name = socket.gethostbyaddr(ip)[0]
            print("Host name:", host_name)
            print("IP address:", ip)
            print("Host name and IP address:", host_name + "/" + ip)
        except socket.herror:
            print("Could not find IP address:", ip)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
