import sqlite3

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''SELECT Indexx.value,Indexx.country, Activity.activity, Period.period, Product.product,Unit.unit FROM Indexx JOIN Activity JOIN 
Period JOIN Product JOIN Unit ON Indexx.activity_id=Activity.id AND Indexx.period_id = Period.id AND Indexx.product_id=Product.id AND Indexx.unit_id=Unit.id
WHERE period=2021 AND product='Petroleum and other liquids' AND activity = 'Consumption' AND unit='thousand barrels per day'
ORDER BY value DESC LIMIT 10''')

print('')
print('Top 10 largest Petroleum consuming in 2021:\n')

for i in cur:
	print(list(i)[1],':',list(i)[0],list(i)[5])

cur.execute('''SELECT Indexx.value,Indexx.country, Activity.activity, Period.period, Product.product, Unit.unit FROM Indexx JOIN Activity JOIN 
Period JOIN Product JOIN Unit ON Indexx.activity_id=Activity.id AND Indexx.period_id = Period.id AND Indexx.product_id=Product.id AND Indexx.unit_id=Unit.id
WHERE product='CO2 emissions' AND country='World' ORDER BY period ASC''')

print('')
print('CO2 Emissions in the world over the time:\n')
for i in cur:
	print(list(i)[3],':',list(i)[0],list(i)[5])

cur.close()