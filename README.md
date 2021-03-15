# RemoteSensor

This Project is about a sensor Platform for our Weekendhome.
![first non breadboard version](https://github.com/MisterD66/RemoteSensor/blob/main/soldered.JPG?raw=true)

## Project description

* The Brain of the Project will be a Raspberry Pi Pico running CircuitPython. 
* For the first Version i will be using a BME280 for monitoring the air pressure, inside Temperature and Humidity.
* A second Temperature Sensor monitoring the outside Air temperature is not specified yet (i was thinking about a DHT22, but when i started it was not supported by CP)
* Future Sensor Options also include a Brightnes sensor.
* For communication i am using a SIM800L module that transmits to my webserver.
* On the webserver side there is a PHP file that gets the Variables from the URL and apend them to a file (maybe write them to a database in the future) also the timestamp for the datapoints is generated on the PHP Server eliminating the need for an RTC on the board

## Problems

* Circuit Python support for the Pico is not full featured yet, there are still some quite important modules missing!
* UART Support was added since i started my project so no problem anymore
* I had to do some edits in the phona library so it get the module working. also there is no command for the sleepmodes of the module, maybe i consider cutting the power to the module while not in use!
* pulsein lib is not supported yet (in the nightly builds its allready available) so most singlewire sensora are not possible yet.
* one of the biggest problems is the "alarm" library that is used for puting the Pico in deepsleep is not available yet! also i didnt see any traces of it in the github so a added a feature request.

## Powerconsumption

* i did some estimation, without any optimisation i get an idle consumption of 40mA
* a full circle of collecting measurements and transmiting them takes about 100s and is using an average of 100mA

i also measured the pico without the GSM module it is about 20mA so i hope to improve that in the future with some sleepmodes!
the other half of the Idle consumption is the 20mA from the gsm module, i hope to implement some kind of power down and power up for the modem!

for my test now i use a single liion cell with 2500mA - with the curent powerconsumption and new measurements every half hour it should last for about 2 days
