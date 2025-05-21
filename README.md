 Socket Threaded Chat Server

This is a simple Python-based chat application that uses **socket programming** and **thread pooling** to handle multiple client connections concurrently.

Description

The project demonstrates how to build a multi-client chat server using Python's built-in `socket`, `threading`, and `concurrent.futures` modules. Each client connects to the server, sends messages, and receives confirmation responses. The server uses a **thread pool** to manage multiple clients efficiently.

Features

- Thread pool 
- Logging of server and client actions.
- Graceful handling of client disconnection.
- Simple bidirectional message system.
- Modular structure with logger configuration and client logic separated.

Setup

1. **Clone the repository:**
   git clone https://github.com/mohamedhamednour/socket-threads.git
   cd socket-threads

   1. Start the server first:  
   make run-server

   2 - start run clinet
   make  make run-client 
      
