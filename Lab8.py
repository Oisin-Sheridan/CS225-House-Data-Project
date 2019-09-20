import geohash2
import sqlite3
from haversine import haversine
'''
InputGeohash = 'ebcdefghebcdefgh'
ErrorList = []
substring = ""
templist = []
ZeroZero = (0.0,0.0)
for i in range(1,len(InputGeohash)+1):
	substring = InputGeohash[0:i]
	templist = geohash2.decode_exactly(substring)
	ErrorPoint = (templist[2],templist[3])
	print(haversine(ZeroZero, ErrorPoint))
'''
conn = sqlite3.connect('HouseDatabase2.db')
c = conn.cursor()
c.execute('SELECT * FROM Sales LIMIT 500')
First500 = c.fetchall()
for k in First500:
	Closest = []
	ClosestDistance = 0
	PropinQuestion = k
	GeohashinQuestion = PropinQuestion[6]
	CurrentGeohash = ""
	c.execute('SELECT * FROM Sales')
	print(k[0])
	for j in c.fetchall():
		if j != k:
			CurrentGeohash = j[6]
			Distance = haversine((k[0]), (j[0]))
			if Distance < ClosestDistance or Distance == 0:
				ClosestDistance = Distance
				Closest = j
	print(Closest)
	print(ClosestDistance)

