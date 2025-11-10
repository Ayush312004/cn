import socket
import os

# Server IP address and port
HOST = '127.0.0.1'
PORT = 12345       

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# File paths for text, audio, and video
file_paths = {
    'text': r'C:\Users\ASUS\OneDrive\Documents\New folder\Myfile2.txt',
    'audio': r'C:\Users\PRATHAM SHEWALE\Desktop\CN\audio.mp3',
    'video': r'C:\Users\PRATHAM SHEWALE\Desktop\CN\video.mp4'
}

while True:
    try:
        # Prompt user to choose the file type
        file_type = input("Enter the type of file to send (text/audio/video or 'exit' to quit): ").lower()

        if file_type == 'exit':
            # Send the exit command to the server
            s.sendto(b'exit', (HOST, PORT))
            print("Exiting client.")
            break

        # Check if the file type is valid
        if file_type in file_paths:
            file_path = file_paths[file_type]

            # Check if the file exists
            if os.path.exists(file_path):
                # Send file type to the server first
                s.sendto(file_type.encode(), (HOST, PORT))

                # Send file data in chunks
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(128)  # Read data in chunks of 128 bytes
                        if not data:
                            break  # Stop reading when no more data
                        s.sendto(data, (HOST, PORT))  # Send the data

                # Send 'EOF' to indicate the end of file
                s.sendto(b'EOF', (HOST, PORT))
                print(f"{file_type.capitalize()} file has been sent successfully.")
            else:
                print("File not found. Please check the file path.")
        else:
            print("Invalid file type entered.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the socket once the loop ends
s.close()



