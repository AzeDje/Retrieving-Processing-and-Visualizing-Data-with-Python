import sqlite3
import json
import codecs

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''SELECT Indexx.value,Indexx.country, Activity.activity, Period.period, Product.product,Unit.unit FROM Indexx JOIN Activity JOIN 
Period JOIN Product JOIN Unit ON Indexx.activity_id=Activity.id AND Indexx.period_id = Period.id AND Indexx.product_id=Product.id AND Indexx.unit_id=Unit.id
WHERE value NOT IN ('w','ie', 'NA','--') AND period=2021 AND product='Petroleum and other liquids' AND activity = 'Consumption' AND unit='thousand barrels per day'
ORDER BY value DESC LIMIT 10''')

fhand = open('databar.js','w')
fhand.write("data1 = [")
count=0
for row in cur:
	value=list(row)[0]
	country=list(row)[1]
	count=count+1
	if count >1:
		fhand.write(',\n')
	fhand.write('{\n'+'Country:'+"'"+country+"'"+',\nValue:'+"'"+str(value)+"'"+'\n}')
fhand.write("\n];\n")
fhand.close()
print('\n')
print (count, 'Records written to databar.js')

cur.execute('''SELECT Indexx.value,Indexx.country, Activity.activity, Period.period, Product.product FROM Indexx JOIN Activity JOIN 
Period JOIN Product ON Indexx.activity_id=Activity.id AND Indexx.period_id = Period.id AND Indexx.product_id=Product.id 
WHERE value NOT IN ('w','ie', 'NA','--') AND product='CO2 emissions' AND country='World' ORDER BY period ASC ''')

fhand = open('dataline.js','w')
fhand.write("data2 = [")
count=0
for row in cur:
	value=list(row)[0]
	period=list(row)[3]
	count=count+1
	if count >1:
		fhand.write(',\n')
	fhand.write('{\n'+'date:'+"'"+str(period)+"'"+',\nvalue:'+"'"+str(value)+"'"+'\n}')
fhand.write("\n];\n")
fhand.close()
cur.close()
print('\n')
print (count, 'Records written to dataline.js')
print ('Open visualize.html to visualize the data in your browser.')

