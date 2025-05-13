import socket
from conf import HOST, PORT
from logger_config import logger_conf


logger = logger_conf(__name__)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        welcome_msg = s.recv(1024).decode()
        logger.info(f"Server: {welcome_msg}")

        while True:
            msg = input("Enter message (type 'exit' to quit): ")
            s.sendall(msg.encode())

            if msg.lower() == "exit":
                logger.info("Disconnected .")
                break

            try:
                data = s.recv(1024)
                if data == b"":
                    logger.warning("Server closed the connection.")
                    break
                else:
                    logger.info(f"Server: {data.decode()}")
            except socket.timeout:
                logger.error("Connection timed out.")
                break

except ConnectionResetError:
    logger.error("server crashed.")
except Exception as e:
    logger.exception(f"Unexpected error occurred: {e}")
