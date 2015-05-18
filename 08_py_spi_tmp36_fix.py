#!/usr/bin/python
 
import spidev
import time
import datetime
import os
 
spi = spidev.SpiDev()
spi.open(0,0)

#datafile = "/home/pi/myweb/public/data.tsv"
# read SPI data from one of the ADC chips such as MCP3008's eight possible inputs (0 thru 7)
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

def checkfile():
	global datafile
	datafile = "/home/pi/myweb/public/data.tsv"
	if (os.path.isfile(datafile) != True):
		f =open(datafile,"w")
		f.write ("date\tHerbie\r\n")
		f.close()
checkfile()

while True:
	#datafile
        rawTemp = readadc(TempSensor)
        # Convert the raw ADC input to milliVolts, degrees Celsius and Fahrenheit
        milliVolts = rawTemp * (3300.0 / 4096.0)
        tempCelsius = float("{0:.1f}".format(((milliVolts - 100.0) / 10.0) - 40.0))
	itempCelsius = int(tempCelsius)
      	t = datetime.datetime.now()
	strDate =  str(t.day) +'-' + str(t.month) + '-' + str(t.year) + ' ' + str(t.hour) + str(t.minute) + str(t.second) 
	
	f = open(datafile,"a")
	f.write (strDate  + "\t" + str(itempCelsius)+ "\r\n")
	f.close()
	
	time.sleep(300) # wait 5 minutes

import sys
sys.exit()
