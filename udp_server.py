import socket
import os  # Import os to open files

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
s.bind((HOST, PORT))
print("Server is listening...")

BUFFER_SIZE = 65535  # Maximum size for a UDP packet

# Define a mapping of file types to proper extensions
file_type_mapping = {
    'audio': 'mp3',     # For audio files
    'video': 'mp4',     # For video files
    'text': 'txt',      # For text files
}

while True:
    print("Waiting for a new file...")

    # Receive file type or exit command
    file_type, addr = s.recvfrom(BUFFER_SIZE)
    file_type = file_type.decode().strip()  # Decode and clean the received file type

    # Check if the client sent the "exit" command
    if file_type.lower() == "exit":
        print("Exit command received. Shutting down the server.")
        break  # Exit the loop to close the server

    # Get the correct extension from the mapping or default to 'bin' if unknown
    file_extension = file_type_mapping.get(file_type, 'bin')
    file_name = f"received_file.{file_extension}"  # Save the file with the appropriate extension

    print(f"Receiving a {file_type} file from {addr}...")

    # Open the file to write binary data
    with open(file_name, 'wb') as f:
        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)  # Receive file data
            if data == b'EOF':  # End of file indicator
                print(f"File has been received and saved as '{file_name}'.")
                break  # Break when the entire file is received
            f.write(data)  # Write the received data to the file

    # Ask the user if they want to open the file
    open_file = input(f"Do you want to open the file '{file_name}'? (yes/no): ").strip().lower()
    
    if open_file == 'yes':
        try:
            # Open the file using the default application
            os.startfile(file_name)  # For Windows (use 'os.system' or 'subprocess' for other OS)
            print(f"Opening the file '{file_name}'...")
        except Exception as e:
            print(f"Error opening file: {e}")
    else:
        print(f"File '{file_name}' has been saved but not opened.")

# Close the socket after the exit command
s.close()
print("Server has been closed.")


