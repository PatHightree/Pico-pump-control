from web_server import *
from pump_control import *

led.off()
start_timers()
try:
    ip = connect()
    connection = open_socket(ip)
    led.on()
    serve(connection)
except KeyboardInterrupt:
    led.off()
    connection.close()
    print('Connection was closed')
    machine.reset()
