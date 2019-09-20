import csv
import sqlite3
import datetime

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
			print(calculatedPrice)
			print(" ")

		else:
			print("No relevant data before this date")