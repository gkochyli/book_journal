#!/usr/bin/env python3 
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('test_database.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
	
def data_entry():
	c.execute("INSERT INTO stuff VALUES(34234, '2014-01-01', 'Python', 343)" )
	conn.commit()
	c.close()
	conn.close()
	
def dynamic_data_entry():
	unix = time.time()
	#date = str(datetime.datetime())#.frotimestamp(unix))#.strftime('%Y-%m-%d %H:%M:%S'))
	date = time.strftime('%Y-%m-%d %H:%M:%S')
	keyword = 'Python'
	value = random.randrange(0,10)
	c.execute("INSERT INTO stuff (unix, datestamp, keyword, value) VALUES (?,?,?,?)", (unix,date,keyword,value))
	conn.commit()
	
def read_data():
	c.execute("SELECT * FROM stuff")
	data = c.fetchall()
	for row in data:
		print(row)
	
#c.execute("DELETE FROM stuff")
'''
create_table()
for i in range(0,10):
	dynamic_data_entry()
	time.sleep(1)
c.close()
conn.close()
'''

#read_data()
c.execute("SELECT * FROM stuff LIMIT 1 OFFSET 3") #return the 4th row !!!
data = c.fetchall()
print(data)
