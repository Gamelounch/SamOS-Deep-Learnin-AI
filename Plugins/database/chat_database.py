#All Rights Reserved
#Anny Changes in this file is on you own risk


import json
import sqlite3
from datetime import datetime

# Deklariert das Paket
timeframe = '2015-01'


sql_transaction = []

connection = sqlite3.connect (' {}.db' .format(timeframe))
c = connection.cursor()

def find_existing_score(pid):
    try:

        sql = "SELECT score FROM parent_reply WHERE parent_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else: return False
    except Exception as e:
        # print("find_parent", e)
        return False

def sql_insert_replace_comment(commentid,parentid,parent,comment,subreddit,time,score)
    try:
        sql = """UPDATE parent_reply SET parent_id = ?, comment_id = ?, parent = ?, comment = ?, subreddit = ?, unix = ?, score = ?, WHERE parent_id =?;""".format(parentid
        transaction_bldr(sql)
    execpt Expection as e:
        print ('s-UPDATE insertion' ,str(e))

    except Exception as e:
        print('replace_comment' ,str(e))


def create_table() :
    c.execute("""CREATE TABLE IF NOT EXIST parent_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT,
    unix INT, score INT) """)

def format_data(data) :
    data = data.replace("\n", " newlinechar ") .replace("\r", " newlinechar ") .replace('"', "'")
    return data

def find_parent(pid) :
    try:

        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1" .format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result [0]
        else : return False
    except Exception as e:
    #print("find_parent", e)
        return False

def acceptable(data) :
    if len(data.split(' ')) > 50 or len(data) <1:
        return False
    elif len(data) >1000:
        return False
    elif data == '[deleted]' or data = '[removed]':
        return False
    else:
        return True


if __name__ == "__main__":
    create_table()
    row_counter = 0
    paired_row = 0

    with open ("C:/Users/uiss-/Downloads/{}/RC_{}".format(timeframe.split ('-')[0], timeframe), buffering=1000) as f:
        for row in f:
            row_counter += 1
            row=json.loads (row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']

            parent_data = find_parent(parent_id)

            if score >= 2:
                if acceptable(body):
                    existing_comment_score = find_existing_score(parent_id)
                    if existing_comment_score :
                        if score > existing_comment_score:
                            sql_insert_replace_comment(comment_id, parent_id, parent_data, body, subreddit, created_utc, score)
                    else:
                        if parent_data:
                            ####
                            sql_insert_has_parent(comment_id, parent_id, parent_data, body, subreddit, created_utc, score)
                        else:
                            ####
                            sql_insert_no_parent(comment_id, parent_id, body, subreddit, created_utc, score)
