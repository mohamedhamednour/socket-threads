import socket
import threading
from conf import HOST, PORT
from logger_config import logger_conf
from service_clinet import chat_client
from concurrent.futures import ThreadPoolExecutor

logger = logger_conf(__name__)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    logger.info(f"Server listening on {HOST}:{PORT}...")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            conn, addr = s.accept()
            logger.info(f"New connection from {addr}")
            executor.submit(chat_client, conn, addr)
