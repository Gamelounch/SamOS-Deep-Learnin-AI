#All Rights Reserved
#Anny Changes in this file is on you own risk


import json
import sqlite3

# Deklariert das Paket
timeframe = '2015-01'
sql_transaction = []

connection = sqlite3.connect('{}.db' .format(timeframe))
c = connection.cursor()

