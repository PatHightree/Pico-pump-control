import network
import socket
from time import sleep
from pump_control import *
import machine

ssid = "Wifi Things"
password = "toekanbakkiethembakikker"

def webpage():
    file = open('./site.html')
    site = file.read()
    file.close()
    return str(site)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    # Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        #print (request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request.find('slider') > -1:
            slider_val = request.split('?')[1]
            print (slider_val)
        html = webpage()
        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()