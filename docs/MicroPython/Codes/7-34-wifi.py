'''
 * Filename    : 7-34-wifi
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import network
import socket
import time
import machine

# WiFi connection
SSID = 'your WiFi name'  # your WiFi name
PASSWORD = 'your WiFi password'  # your WiFi password

# connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Create WLAN objects using STA mode (client mode)
    wlan.active(True)  # activate WLAN interface
    wlan.connect(ssid, password)  # Connect to the specified WiFi network

    timeout = 10  # Connect timeout duration in seconds
    while not wlan.isconnected() and timeout > 0:  # If the connection fails and the timeout period does not expire, check the connection status again
        print("Connecting to WiFi...")
        time.sleep(1)
        timeout -= 1

    if not wlan.isconnected():  # If the connection is not successful after timeout, an exception is thrown
        raise Exception("Could not connect to WiFi")
    
    print('Network config:', wlan.ifconfig())  # Output network configuration (IP address, subnet mask, gateway, and DNS)
    print('Connected to WiFi, IP address:', wlan.ifconfig()[0])  # output the IP address of the successful connection
    return wlan

# create HTML page
def web_page():
    html = """<html>
    <head>
        <title>ESP32 Web Server</title>
    </head>
    <body>
        <h1>Hello World</h1>
    </body>
    </html>"""
    return html  # Return a simple HTML page with "Hello World"

# Start the Web server
def start_server():
    wlan = connect_wifi(SSID, PASSWORD)  # connect to WiFi
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]  # Obtain the local IP address and port 80
    s = socket.socket()  # Create a socket object
    s.bind(addr)  # Bind sockets to addresses and ports
    s.listen(5)  # Start listening for incoming connections. The maximum number of connections is 5
    print('Listening on', addr)  # Print the address and port on which the server is listening

    while True:
        cl, addr = s.accept()  # Accept a client connection
        print('Client connected from', addr)  # Print the address of the client
        request = cl.recv(1024)  # Receive client requests, up to 1024 bytes
        request = str(request)  # Convert the request to a string
        print('Content = %s' % request)  # Print request content
        
        response = web_page()  # Generate HTML response
        cl.send('HTTP/1.1 200 OK\n')  # Send the HTTP response header
        cl.send('Content-Type: text/html\n')  # Specify the content type as HTML
        cl.send('Connection: close\n\n')  # Close connection
        cl.sendall(response)  # Send HTML page content
        cl.close()  # Close the client connection

# Run server
try:
    start_server()  # Try starting the Web server
except Exception as e:
    print('Failed to start server:', e)  # If the startup fails, an error message is displayed
    machine.reset()  # Restart the device to try to reconnect
