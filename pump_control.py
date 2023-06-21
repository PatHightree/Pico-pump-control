from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
pond_pin = Pin(0, Pin.OUT)
waterfall_pin = Pin(1, Pin.OUT)
pond_wait_timer = Timer()
pond_fill_timer = Timer()
waterfll_wait_timer = Timer()
waterfall_purge_timer = Timer()

# Configuration variables
pond_wait_seconds = 3
pond_fill_seconds = 1
pond_purge_repeat = 2
waterfall_wait_seconds = 2
waterfall_purge_seconds = 1

# Runtime variables
pond_wait_millis = 999
pond_fill_millis = 999
waterfall_wait_millis = 999
waterfall_purge_millis = 999

def calculate_periods():
    global pond_wait_millis, pond_fill_millis, waterfall_wait_millis, waterfall_purge_millis
    pond_wait_millis = int(pond_wait_seconds * 1000)
    pond_fill_millis = int(pond_fill_seconds * 1000)
    waterfall_wait_millis = int(waterfall_wait_seconds * 1000)
    waterfall_purge_millis = int(waterfall_purge_seconds * 1000)

def pond_wait(pond_fill_timer):
    pond_pin.off()
    #print('pond off')
    pond_wait_timer.init(period=int(pond_wait_millis), mode=Timer.ONE_SHOT, callback=pond_fill)    

def pond_fill(pond_wait_timer):
    #print('pond on')
    pond_pin.on()
    pond_fill_timer.init(period=pond_fill_millis, mode=Timer.ONE_SHOT, callback=pond_wait)
    
def set_pond_wait(seconds):
    pond_wait_seconds = seconds
    restart_timers()
    
def set_pond_fill(seconds):
    pond_fill_seconds = seconds
    restart_timers()

def waterfall_wait(pond_purge_timer):
    #print('waterfall off')
    waterfall_pin.off()
    waterfll_wait_timer.init(period=waterfall_wait_millis, mode=Timer.ONE_SHOT, callback=waterfall_purge)    

def waterfall_purge(pond_wait_timer):
    #print('waterfall on')
    waterfall_pin.on()
    waterfall_purge_timer.init(period=waterfall_purge_millis, mode=Timer.ONE_SHOT, callback=waterfall_wait)

def set_waterfall_wait(seconds):
    waterfall_wait_seconds = seconds
    restart_timers()
    
def set_waterfall_purge(seconds):
    waterfall_purge_seconds = seconds
    restart_timers()

def start_timers():
    global pond_fill_timer, waterfall_purge_timer
    calculate_periods()
    pond_wait(pond_fill_timer)
    waterfall_wait(waterfall_purge_timer)
    
def stop_timers():
    pond_wait_timer.deinit()
    pond_fill_timer.deinit()
    waterfll_wait_timer.deinit()
    waterfall_purge_timer.deinit()

def restart_timers():
    stop_timers()
    start_timers()

#start_timers(pond_fill_timer, waterfall_purge_timer)
