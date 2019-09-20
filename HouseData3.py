import csv
import sqlite3
import datetime
import geohash2
with open('HouseData.csv',encoding='MAC_ROMAN') as HouseData:
	CSVreader = csv.reader(HouseData, delimiter=',')
	Rows = []
	for row in CSVreader:
		Rows.append(row)

conn = sqlite3.connect('HouseDatabase2.db')
c = conn.cursor()
c.execute("DROP TABLE Sales")
c.execute('''CREATE TABLE Sales
			 (LatLon text, Address text, County text, SellDate date, SalePrice real, OrdinalTime real, Geohash text)''')
dateString = ""
counter = 0
CurrentGeohash = ""
for i in Rows:
	if counter!=0:
		j = [int(e) for e in str(i[3]).split('/')]
		k = datetime.date(j[2],j[1],j[0]).toordinal()
		i.append(k)
		try:
			LatLonPoint = [float(l) for l in i[0].split(',')]
			CurrentGeohash = geohash2.encode(LatLonPoint[0], LatLonPoint[1], precision=16)
			i.append(CurrentGeohash)
			c.execute("INSERT INTO Sales VALUES (?,?,?,?,?,?,?)",i)
		except:
			print(i)
	if counter==0:
		counter+=1

conn.commit()
