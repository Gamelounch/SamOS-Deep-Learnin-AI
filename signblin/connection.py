#!/usr/bin/python
import urllib2
import urllib
import time
from datetime import datetime
import sys
import os


# Geschwindigkeit messen
def measure(url="http://www.speedtestx.de/testfiles/data_500mb.test", intervall=2, buf=10):


f = urllib2.urlopen(url)
tStart = datetime.now()
amount = 0
x = 0

while ((len(f.read(buf)) == buf) & (x <= 60)):
    tEnd = datetime.now()
dif = (tEnd - tStart).total_seconds()

if (dif >= intervall):

    # print (time.strftime("%H:%M:%S; ")),((((amount/intervall)/1000.00)*8)/1024), "Mbit/s;"
    amount = 0
    tStart = datetime.now()
    x = x + 1

else:
    amount = amount + buf

try:
    measure(buf=1024, intervall=2)


except  KeyboardInterrupt:
    exit(0)