import json
import sqlite3
import time

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

conn2 = sqlite3.connect('clean.sqlite')
cur2 = conn2.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Product (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, product TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Period (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, period DATE UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Activity (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, activity TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Unit (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, unit TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Indexx ( clean_id INTEGER UNIQUE,value REAL, country TEXT, product_id INTEGER,
period_id INTEGER,activity_id INTEGER, unit_id INTEGER )''')

cur.execute('SELECT max(clean_id) FROM Indexx' )
cur2.execute('SELECT max(id) FROM Clean' )
try:
	maxid1=cur.fetchone()[0]
	maxid2=cur2.fetchone()[0]
except:
	pass
if maxid1 is None :
	count = 0
else:
	count = maxid1
remain=maxid2-count
if maxid1 == maxid2:
	print('')
	print('Process already finished.')
	print(maxid1,'Rows already inserted into database (index.sqlite).')
	print(remain,'Row remaining.')
	cur.close()
	cur2.close()
	quit()

cur2.execute('''SELECT id,value,country, productname, activityname,period,unitname FROM Clean''' )
print('')
print('Data loading...')
try:
	row = cur2.fetchall()
except KeyboardInterrupt:
	print('')
	print('Program interrupted by user...')
	print('Process not yet finished...')
	print(count,'Rows already inserted into database (index.sqlite).')
	print(remain,'Rows remaining...')
	cur.close()
	cur2.close()
	quit()

try:
	for i,j,k,l,m,n,o in row:
		if i <= count:
			continue
		cur.execute('''INSERT OR IGNORE INTO Product (product) VALUES (?)''',(l,))
		cur.execute('''SELECT id FROM Product WHERE product=?''',(l,) )
		product_id = cur.fetchone()[0]

		cur.execute('''INSERT OR IGNORE INTO Activity (activity) VALUES (?)''',(m,))
		cur.execute('''SELECT id FROM Activity WHERE activity=?''',(m,) )
		activity_id = cur.fetchone()[0]

		cur.execute('''INSERT OR IGNORE INTO Period (period) VALUES (?)''',(n,))
		cur.execute('''SELECT id FROM Period WHERE period=?''',(n,) )
		period_id = cur.fetchone()[0]

		cur.execute('''INSERT OR IGNORE INTO Unit (unit) VALUES (?)''',(o,))
		cur.execute('''SELECT id FROM Unit WHERE unit=?''',(o,) )
		unit_id = cur.fetchone()[0]
		
		cur.execute('''INSERT OR IGNORE INTO Indexx (clean_id,value,country,product_id,period_id,activity_id,unit_id) 
			VALUES (?,?,?,?,?,?,?)''',(i,j,k,product_id,period_id,activity_id,unit_id) )
		count=count+1
		remain=remain-1
		print('')
		print(remain,'Rows remaining...')
		
	conn.commit()
	print('')
	print('Process finished.')
	print(count,'Rows inserted into database (index.sqlite).')
	print(remain,'Row remaining.')
	time.sleep(5)	

except KeyboardInterrupt:
	conn.commit()
	print('')
	print('Program interrupted by user...')
	print('Process not yet finished...')
	print(count,'Rows inserted into database (index.sqlite).')
	print(remain,'Rows remaining...')
	time.sleep(5)
	cur.close()
	cur2.close()
	quit()

cur.close()
cur2.close()	