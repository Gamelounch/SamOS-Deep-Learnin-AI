# All Rights Reserved
# Anny Changes in this file is on you own risk


import json
import sqlite3

# Deklariert das Paket
timeframe = '2015-01'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()


# This will Create a New Database Table if not Exist
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
    comment TEXT, subreddit TEXT, unix INT, score INT)""")


def format_data(data):
    data = data.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"', "'")
    return data


if __name__ == "__main__":
    create_table()
    row_counter = 0
    paired_rows = 0

    with open("C:\Users\uiss-\Downloads\RC_2015-01/{}/RC_{}".format(timeframe.split('-')[0], timeframe),
              buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.load(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']

            parent_data = find_parent(parent_id)
