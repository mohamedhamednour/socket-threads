from logger_config import logger_conf

logger = logger_conf(__name__)


def chat_client(conn, addr):
    conn.sendall("Thank you for connecting!".encode())

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data or data.lower() == "exit":
                logger.info(f"Client {addr} has left the chat.")
                break

            logger.info(f"Received from client {addr}: {data}")
            conn.sendall(f"Message received: {data}".encode())
    except ConnectionError:
        logger.warning(f"Client {addr} disconnected.")
    finally:
        conn.close()
