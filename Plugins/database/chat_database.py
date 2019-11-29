#All Rights Reserved
#Anny Changes in this file is on you own risk


import json
import sqlite3

# Deklariert das Paket
timeframe = '2015-01'
sql_transaction = []

connection = sqlite3.connect('{}.db' .format(timeframe))
c = connection.cursor()
#This will Create a New Database Table if not Exist
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
    comment TEXT, subreddit TEXT, unix INT, score INT)""")

if __name__ == "__main__":
    create_table()
