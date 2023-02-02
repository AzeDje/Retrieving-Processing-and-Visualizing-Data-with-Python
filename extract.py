import urllib.request, urllib.parse, urllib.error
import ssl
import json
import sqlite3
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('energydata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Data ( id INTEGER NOT NULL PRIMARY KEY, period DATE,
	country TEXT, productname TEXT,activityname TEXT,unitname TEXT, value REAL )''')

cur.execute('SELECT max(id) FROM Data' )
try:
	row = cur.fetchone()[0]
	if row is None :
		offset = 0
		length = 5000
		id = 0
	else:
		id = row
		offset = row 
		length = 5000
except:
	offset = 0
	length = 5000

while True:
	apikey='AthfSuSeC---------------------LrBkYr' #you have to register at https://www.eia.gov/opendata/register.php to get your api_key.
	param=dict()
	param['frequency']='annual'
	param['data[0]']='value'
	param['offset']=offset
	param['length']=length
	param['api_key']=apikey

	api='https://api.eia.gov/v2/international/data/?'
	url=api+ urllib.parse.urlencode(param)
	print('\nRetrieving',url)
	try:
		databyte = urllib.request.urlopen(url, context=ctx).read()
	except KeyboardInterrupt:
		print('')
		print('Program interrupted by user...')
		print('Process not yet finished')
		print(id,'Rows inserted into database (energydata.sqlite).')
		cur.close()
		quit()
	except:
		print('')
		print('ERROR!!! Please check URL parameters\n')
		cur.close()
		quit()
	datastr=databyte.decode()
	print('Retrieved',len(datastr), 'characters')
	try:
		datajs = json.loads(datastr)
	except:
		datajs = None
	if not datajs :
		print('')
		print('ERROR!!! Failure to retrieve JSON DATA\n')
		print(datastr)
		cur.close()
		quit()
	count=list()

	try:	
		count.append(id)
		for d in datajs['response']['data']:
			period=d['period']
			productname=d['productName']
			activityname=d['activityName']
			countryregionname=d['countryRegionName']
			unitname=d['unitName']
			value=d['value']
			id=id+1
			print('')
			print('Country Region Name:',countryregionname)
			print('Product Name:',productname)
			print('Period:',period)
			print('Activity Name:',activityname)
			print('Value:',value)
			print('Unit:',unitname)
			cur.execute('INSERT INTO Data (id, period ,	country , productname,activityname ,unitname , value) VALUES ( ?, ?, ?,?,?,?,? )', (id,period,countryregionname,productname,activityname ,unitname , value))
		conn.commit()

		if len(datajs['response']['data'])==0:
			print('')
			print('Process finished.')
			print(id,'Rows inserted into database (energydata.sqlite).')
			cur.close()
			quit()

		print('')
		print(id,'Rows inserted into database (energydata.sqlite).')
		print('In Process...')
		time.sleep(1)
	except KeyboardInterrupt:
		conn.commit()
		print('')
		print('Program interrupted by user...')
		print('Process not yet finished')
		if id-count[len(count)-1]==5000:
			print(id,'Rows inserted into database (energydata.sqlite).')
		else:
			print(id-1,'Rows inserted into database (energydata.sqlite).')
		time.sleep(1)
		cur.close()
		quit()
		
	offset=offset+5000
cur.close()	



