import sqlite3
import pandas as pd

conn = sqlite3.connect('clean.sqlite')
cur = conn.cursor()

conn2 = sqlite3.connect('energydata.sqlite')
cur2 = conn2.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Clean ( id INTEGER NOT NULL PRIMARY KEY UNIQUE, period DATE, country TEXT, 
	productname TEXT,activityname TEXT,unitname TEXT, value REAL )''')

cur2.execute('''SELECT period,country,productname,activityname,unitname,value FROM Data ORDER BY value DESC ''')

print('')
print('Data loading...')
try:
	df = pd.DataFrame(cur2.fetchall(), columns = ['period', 'country','productname','activityname','unitname','value'])
	dfnew = df.drop_duplicates()
	dfnew.drop(dfnew[dfnew['country'] == 'OECD - North America'].index, inplace = True)
	dfnew.drop(dfnew[dfnew['country'] == 'IEO - Africa'].index, inplace = True)
	dfnew.drop(dfnew[dfnew['country'] == 'IEO OECD - Europe'].index, inplace = True)
	dfnew.drop(dfnew[dfnew['country'] == 'IEO - Middle East'].index, inplace = True)
	dfnew.drop(dfnew[dfnew['country'] == 'OECD - Europe'].index, inplace = True)
	dfnew = dfnew.drop_duplicates(subset=["period", "country",'productname','activityname','unitname'], keep='first')
except KeyboardInterrupt:
	print('')
	print('Program interrupted by user...')
	print('Process not yet finished...')
	cur.close()
	cur2.close()
	quit()

cur.execute('SELECT max(id) FROM Clean' )
cur2.execute('SELECT max(id) FROM Data' )
try:
	maxid1=cur.fetchone()[0]
	maxid2=cur2.fetchone()[0]
except:
	pass

if maxid2-(maxid2-len(dfnew))==maxid1:
	print('')
	print('Process already finished.')
	print(maxid1,'Rows inserted into database (clean.sqlite).')
	cur.close()
	cur2.close()
	quit()

dfnew['value'] = dfnew['value'].replace(['--', 'NA','w','ie','p'], 0)
df['value'] = dfnew['value'].astype(float)
dfnew['value']=dfnew['value'].round(1)

id=list()
count=1
try:
	print('')
	print('In Process...')
	while count <= len(dfnew):
		id.append(count)
		if count==len(dfnew):
			break
		count=count+1
	dfnew.insert(0, 'id', id)

	print('')
	print('Copying to database (clean.sqlite)...')
	dfnew.to_sql('Clean', conn, if_exists='replace', index = False)
except KeyboardInterrupt:
	print('')
	print('Program interrupted by user...')
	print('Process not yet finished...')
	cur.close()
	cur2.close()
	quit()

cur.execute('''SELECT max(id) FROM Clean''')
try:
	maxid=cur.fetchone()[0]
except:
	print('')
	print('Fail! Something went wrong! Please repeat the process.')
	cur.close()
	cur2.close()
	quit()
if maxid != len(dfnew):
	print('')
	print('Fail! Something went wrong! Try repeating the process.')
	cur.close()
	cur2.close()
	quit()

print('')
print('Process finished.')
print(count,'Rows inserted into database (clean.sqlite).')

cur.close()
cur2.close()
	