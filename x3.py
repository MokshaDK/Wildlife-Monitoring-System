import socket
import os
import zipfile
import shutil
import predict_bird

def zip_directory(directory_name, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, start=directory_name))


def process_files(input_dir, output_dir):
    predict_bird.predict(input_dir)


def unzip_file(zip_path, extract_to):
    """
    Unzips the file at zip_path to the directory specified by extract_to.
    """
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
        
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        
    print(f"Files have been extracted to {extract_to}")

def receive_file(file_path, host, port):
    """
    Listens for an incoming file transfer and saves the file to file_path.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        print(f"Listening on {host}:{port} for incoming files...")
        conn, addr = sock.accept()
        with conn:
            print(f"Connection established with {addr}")
            with open(file_path, 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print(f"File received and saved as {file_path}")
def send_file_back(file_path, host, port):
    """
    Sends the specified file to the given host and port using a TCP socket.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host, port))
            with open(file_path, 'rb') as file:
                sock.sendfile(file)
            print(f"File {file_path} has been sent back to {host}:{port}")
        except Exception as e:
            print(f"Failed to send {file_path} back to {host}:{port}. Error: {str(e)}")
def delete_file(file_path):
    # Check if file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"File {file_path} does not exist.")


if __name__ == "__main__":
    file_path = 'received_user_input_x.zip'  # The file path to save the received zip file
    host = 'localhost'  # The host IP address to bind to
    port = 12346  # The port to listen on

    input_dir = "X_INPUT"  # The directory to extract the zip contents to
    output_dir = "X_OUTPUT"  # The directory to save processed files to

    # Receive a file transfer
    receive_file(file_path, host, port)
    
    # Unzip the received file
    unzip_file(file_path, input_dir)
    
    # Process the unzipped files
    process_files(input_dir, output_dir)

    
    zip_directory(output_dir,"x.zip")
    send_file_back("x.zip", 'localhost', 12349)
    delete_file('received_user_input_x.zip')
    delete_file('x.zip')


