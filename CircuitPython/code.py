#import alarm
#import machine
import time
import board
import adafruit_bh1750
import busio
import displayio
import terminalio
import adafruit_ssd1306
import adafruit_bme280
from analogio import AnalogIn
import digitalio
import adafruit_requests as requests
from adafruit_fona.adafruit_fona import FONA
import adafruit_fona.adafruit_fona_network as network
import adafruit_fona.adafruit_fona_socket as cellular_socket
from secrets import secrets
print("V1")
JSON_URL = "http://www.snerz.at/iot/index.php?light=222"

# Create a serial connection for the FONA connection
uart = busio.UART(board.GP4, board.GP5)
rst = digitalio.DigitalInOut(board.GP3)


analog_in = AnalogIn(board.A3)

print("Create Sens!")
i2c = busio.I2C(scl=board.GP21, frequency = 50000, sda=board.GP20)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
lux_sens = adafruit_bh1750.BH1750(i2c)
pth_sens = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

start = time.monotonic()
display.fill(0)
display.show()

display.show()

pth_sens.sea_level_pressure = 1013.25

#while True:
now = time.monotonic()
ft=now-start
start = time.monotonic()
voltage = round(analog_in.value /6553.6 ,3)
print("%.2f Lux" % lux_sens.lux)
display.text("%.2f Lux" % lux_sens.lux, 0, 0, 1)
display.text("%.2f C" % pth_sens.temperature, 0, 9, 1)
display.text("%.2f rH" % pth_sens.relative_humidity, 0, 18, 1)
display.text("%.2f hPa" % pth_sens.pressure, 0, 27, 1)
display.text("%.2f m" % pth_sens.altitude, 0, 36, 1)
display.text("%.3f V" % voltage, 0, 46, 1)
display.show()
#fps=1/ft
#display.text("%.2f fps" % fps, 0, 55, 1)
#machine.reset()
#display.fill(0)
print("Start Modem")
fona = FONA(uart, rst)

network = network.CELLULAR(
    fona, (secrets["apn"], secrets["apn_username"], secrets["apn_password"])
)

print(fona.iemi)
#display.text("%.2f Lux" % fona.iemi, 64, 0, 1)

print(fona.iccid)
print(fona.network_status)
while not fona.network_status == 2:
    #print("Attaching to network...")
    print(fona.network_status)
    time.sleep(0.5)
print(fona.network_status)
print("Attached!")
display.text("Attatched" , 64, 0, 1)
display.show()

while not network.is_connected:
    print("Connecting to network...")
    network.connect()
    time.sleep(0.5)
print("Network Connected!")
display.text("Connected" , 64, 9, 1)
display.show()

print("My IP address is:", fona.local_ip)
#print("IP lookup adafruit.com: %s" % fona.get_host_by_name("adafruit.com"))
display.text(fona.local_ip , 64, 18, 1)
display.show()

# Initialize a requests object with a socket and cellular interface
requests.set_socket(cellular_socket, fona)

print("Fetching json from", JSON_URL)
r = requests.get(JSON_URL)
print("-" * 40)
print(r.json())
print("-" * 40)
r.close()
fona.reset()
print("Done!")
display.text("Done" , 64, 27, 1)
display.show()
time.sleep(1)
while True:
    display.fill(0)
    display.text("sleep." , 60, 20, 1)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.text("sleep.." , 60, 20, 1)
    display.show()
    time.sleep(1)
    display.fill(0)
    display.text("sleep..." , 60, 20, 1)
    display.show()
    time.sleep(1)

#time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)
#alarm.exit_and_deep_sleep_until_alarms(time_alarm)
