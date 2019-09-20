import csv
import sqlite3
import datetime
#import geohash2


conn = sqlite3.connect('HouseDatabase2.db')
c = conn.cursor()
c.execute("SELECT * FROM SALES")
fullData = c.fetchall()

'''
with open('InputData.csv',encoding='MAC_ROMAN') as InputData:
	CSVreader = csv.reader(InputData, delimiter=',')
	InputTable = []
	for row in CSVreader:
		InputTable.append(row)

dateString = ""
counter = 0
CurrentGeohash = ""
for m in range(len(InputTable)):
	if counter!=0:
		j = [int(e) for e in str(InputTable[m][3]).split('/')]
		k = datetime.date(j[2],j[1],j[0]).toordinal()
		InputTable[m].append(k)
		LatLonPoint = [float(l) for l in InputTable[m][0].split(',')]
		CurrentGeohash = geohash2.encode(LatLonPoint[0], LatLonPoint[1], precision=16)
		InputTable[m].append(CurrentGeohash)
	if counter==0:
		counter+=1
'''
InputTable = fullData
totalError = 0
numErrors = 0
mistakelist = []
try:
	for i in InputTable:
		totalWeight = 0
		totalSum = 0
		if i[5]>=734138:
			for j in fullData:
				if j[1] == i[1]:
					totalSum==j[4]+(i[5]-j[5])
					totalWeight==1
					break
				elif j[5] >= i[5]:
					break

				k = 16
				geohashSimilarity = 0
				while k > 0:
					if j[6][:k] == i[6][:k]:
						geohashSimilarity = k
						k = 1
					k -= 1

				if geohashSimilarity>=8:
					timeDifference = i[5] - j[5]
					timeWeight = 100-(timeDifference/15)
					totalWeight += geohashSimilarity*timeWeight
					totalSum += j[4]*geohashSimilarity*timeWeight

			if totalWeight>0:
				calculatedPrice = totalSum/totalWeight
				percentageError = ((calculatedPrice-i[4])*100)/i[4]
				print(i[3])
				print(i[4])
				print(calculatedPrice)
				print(percentageError)
				print(" ")

				totalError += abs(percentageError)
				numErrors += 1
				'''
				if percentageError<=200:
					totalError += percentageError
					numErrors += 1
				else:
					mistakelist.append(i[1])
					mistakelist.append(str(i[3]))
					mistakelist.append(str(i[4]))
					mistakelist.append(str(calculatedPrice))
					mistakelist.append(str(percentageError))
				'''


except:
	for k in mistakelist:
		print(k)
	print(" ")
	print(totalError/numErrors)

