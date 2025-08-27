'''
 * Filename    : 3-38-intelligentConsole
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import network
import socket
import time
import machine
import json
from machine import Pin, PWM, ADC, SoftI2C
import aht20

# WiFi connection information
SSID = 'ChinaNet_2.4G'  # your WiFi name
PASSWORD = 'ChinaNet@233'  # your WiFi password


# Initialize executer
ledRed = Pin(23, Pin.OUT)
ledYellow = Pin(26, Pin.OUT)
ledGreen = Pin(27, Pin.OUT)

servo = PWM(Pin(25), freq=50)

MA = Pin(18, Pin.OUT)
MB = Pin(17, Pin.OUT)

# Initialize sensor
light_sensor = ADC(Pin(36))
light_sensor.atten(ADC.ATTN_11DB)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
aht20Sensor = aht20.AHT20(i2c)
# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    timeout = 10
    while not wlan.isconnected() and timeout > 0:
        print("Connecting to WiFi...")
        time.sleep(1)
        timeout -= 1
    
    if not wlan.isconnected():
        raise Exception("Could not connect to WiFi")
    
    print('Network config:', wlan.ifconfig())
    print('Connected to WiFi, IP address:', wlan.ifconfig()[0])
    return wlan

# Create HTML page
def web_page(light, temp, hum):
    html = f"""<html>
    <head>
        <title>ESP32 Control</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; }}
            button {{ padding: 10px 20px; font-size: 16px; margin: 10px; }}
        </style>
        <script>
            function sendRequest(action) {{
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/" + action, true);
                xhr.send();
            }}
            function updateData() {{
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "/sensor_data", true);
                xhr.onload = function() {{
                    if (xhr.status == 200) {{
                        var data = JSON.parse(xhr.responseText);
                        document.getElementById('light').innerText = data.light;
                        document.getElementById('temperature').innerText = data.temperature;
                        document.getElementById('humidity').innerText = data.humidity;
                    }}
                }};
                xhr.send();
            }}
            setInterval(updateData, 1000);
        </script>
    </head>
    <body>
        <h1>ESP32 Control</h1>
        <div>Light Sensor: <span id="light">{light}</span></div>
        <div>Temperature: <span id="temperature">{temp}</span> C</div>
        <div>Humidity: <span id="humidity">{hum}</span> %</div>
        <button onclick="sendRequest('led_on')">LED Red ON</button>
        <button onclick="sendRequest('led_off')">LED Red OFF</button><br>
        <button onclick="sendRequest('ledYellow_on')">LED Yellow ON</button>
        <button onclick="sendRequest('ledYellow_off')">LED Yellow OFF</button><br>
        <button onclick="sendRequest('ledGreen_on')">LED Green ON</button>
        <button onclick="sendRequest('ledGreen_off')">LED Green OFF</button><br>
        <button onclick="sendRequest('servo_left')">Servo Left</button>
        <button onclick="sendRequest('servo_right')">Servo Right</button><br>
        <button onclick="sendRequest('fan_on')">Fan ON</button>
        <button onclick="sendRequest('fan_off')">Fan OFF</button>
    </body>
    </html>"""
    return html

# Control actuator
def handle_request(request):
    if 'led_on' in request:
        ledRed.value(1)
    elif 'led_off' in request:
        ledRed.value(0)
    elif 'ledYellow_on' in request:
        ledYellow.value(1)
    elif 'ledYellow_off' in request:
        ledYellow.value(0)
    elif 'ledGreen_on' in request:
        ledGreen.value(1)
    elif 'ledGreen_off' in request:
        ledGreen.value(0)
    elif 'servo_left' in request:
        servo.duty(30)  # rotate to left
    elif 'servo_right' in request:
        servo.duty(120)  # rotate to right
    elif 'fan_on' in request:
        MA.value(1)
        MB.value(0)
    elif 'fan_off' in request:
        MA.value(0)
        MB.value(0)

# Start the Web server
def start_server():
    wlan = connect_wifi(SSID, PASSWORD)
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        
        if 'GET /sensor_data' in request:
            light_value = light_sensor.read()
            temperature, humidity = aht20Sensor.read_temperature_humidity()
            sensor_data = {
                'light': light_value,
                'temperature': temperature,
                'humidity': humidity
            }

            response = 'HTTP/1.1 200 OK\nContent-Type: application/json\n\n'
            response += json.dumps(sensor_data)
            cl.send(response)
        else:
            light_value = light_sensor.read()
            temperature, humidity = aht20Sensor.read_temperature_humidity()
            response = web_page(light_value, temperature, humidity)
            cl.send('HTTP/1.1 200 OK\n')
            cl.send('Content-Type: text/html\n')
            cl.send('Connection: close\n\n')
            cl.sendall(response)
        
        handle_request(request)
        cl.close()

# run server
try:
    start_server()
except Exception as e:
    print('Failed to start server:', e)
    machine.reset()
