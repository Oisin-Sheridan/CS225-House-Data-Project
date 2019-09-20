import csv
import sqlite3
import datetime
with open('HouseData.csv',encoding='MAC_ROMAN') as HouseData:
	CSVreader = csv.reader(HouseData, delimiter=',')
	Rows = []
	for row in CSVreader:
		Rows.append(row)

conn = sqlite3.connect('HouseDatabase.db')
c = conn.cursor()
c.execute("DROP TABLE Sales")
c.execute('''CREATE TABLE Sales
             (LatLon text, Address text, County text, SellDate date, SalePrice real, OrdinalTime real)''')
dateString = ""
counter = 0
for i in Rows:
	if counter!=0:
		j = [int(e) for e in str(i[3]).split('/')]
		k = datetime.date(j[2],j[1],j[0]).toordinal()
		i.append(k)
		c.execute("INSERT INTO Sales VALUES (?,?,?,?,?,?)",i)
	if counter==0:
		counter+=1

conn.commit()