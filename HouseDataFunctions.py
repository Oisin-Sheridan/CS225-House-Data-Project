import sqlite3
import datetime

conn = sqlite3.connect('HouseDatabase.db')
c = conn.cursor()

#(1)Prints all House Data between 10/9/2017 and 10/10/2017

for i in c.execute('SELECT * FROM Sales'):
	j = [int(e) for e in str(i[3]).split("/")]
	if datetime.date(j[2],j[1],j[0])>=datetime.date(2017,9,10) and datetime.date(j[2],j[1],j[0])<=datetime.date(2017,10,10):
		print(i)

#(2)Prints all House Data where 200000<=Sale Price<=277000

for k in c.execute('SELECT * FROM Sales WHERE SalePrice>=200000'):
	if int(k[4])<=277000:
		print(k)

#(3)Prints the first row with SalePrice>1,000,000

c.execute('SELECT * FROM Sales WHERE SalePrice>=1000000')
print(c.fetchone())

#(4)Prints the mean sale price for January 2018

c.execute('SELECT AVG(SalePrice) FROM Sales WHERE OrdinalTime BETWEEN 736695 AND 736725')
print(c.fetchall())

#(5)Prints the sale dates and sale prices from June 2016 ordered from highest price to lowest price

c.execute('SELECT * FROM Sales WHERE OrdinalTime BETWEEN 736116 AND 736145 ORDER BY SalePrice')
print(c.fetchall())

#(6)Prints out the number of houses in the entire database with sale price greater than 400,000

ticker = 0
for l in c.execute('SELECT * FROM Sales WHERE SalePrice>400000'):
	ticker+=1
print(ticker)

#(7)Calculates the percentage change in the mean sale price from February 2018 to March 2018

c.execute('SELECT AVG(SalePrice) FROM Sales WHERE OrdinalTime BETWEEN 736726 AND 736753')
FebAverage = c.fetchall()
c.execute('SELECT AVG(SalePrice) FROM Sales WHERE OrdinalTime BETWEEN 736754 AND 736784')
MarAverage = c.fetchall()
Change = FebAverage[0][0]-MarAverage[0][0]
print((Change/FebAverage[0][0])*100)

#(8)Calculates the percentage change in the average sale price across all of 2015 and all of 2016
c.execute('SELECT AVG(SalePrice) FROM Sales WHERE OrdinalTime BETWEEN 735599 AND 735963')
Average15 = c.fetchall()
c.execute('SELECT AVG(SalePrice) FROM Sales WHERE OrdinalTime BETWEEN 735964 AND 736329')
Average16 = c.fetchall()
Change = Average15[0][0]-Average16[0][0]
print((Change/Average15[0][0])*100)