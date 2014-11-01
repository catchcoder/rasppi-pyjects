#!/usr/bin/python
 
import spidev
import time
 
spi = spidev.SpiDev()
spi.open(0,0)
 
# read SPI data from one of the MCP3008's eight possible inputs (0 thru 7)
def readadc(adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        r = spi.xfer2([1,(8+adcnum)<<4,0])
	#print r
	#print str([1,(8+adcnum)<<4,0])
        adcout = ((r[1]&3) << 8) + r[2]
        return adcout
 
# TMP36 temperature sensor connected to ADC input 0
TempSensor = 0
temp = 0
while True:
        rawTemp = readadc(TempSensor)
        # Convert the raw ADC input to milliVolts, degrees Celsius and Fahrenheit
        milliVolts = rawTemp * (3300.0 / 4096.0)
        tempCelsius = int(((milliVolts - 100.0) / 10.0) - 40.0)
        #tempFahrenheit = (tempCelsius * 9.0 / 5.0 ) + 32
	if temp <> tempCelsius:
		print ("Temperature %s" % str(tempCelsius))
		temp = tempCelsius

	#print ('-----') 
        #print "raw temp=", rawTemp
        #print "mV=", milliVolts 
	#print "Celsius=", int(tempCelsius)
        #print "Fahrenheit=", int(tempFahrenheit)
 
        time.sleep(0.1)
