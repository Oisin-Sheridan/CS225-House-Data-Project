import csv
import sqlite3
a = 0
with open('HouseData.csv') as HouseData:
	CSVreader = csv.reader(HouseData, delimiter=',')
	Rows = []
	try:
		for row in CSVreader:
			Rows.append(row)
	except:
		print(row)
		try:
			for row in CSVreader:
				Rows.append(row)
		except:
			try:
				for row in CSVreader:
					if a ==0:
						print(row)
					Rows.append(row)
					a+=1
			except:
				try:
					for row in CSVreader:
						Rows.append(row)
				except:
					try:
						for row in CSVreader:
							Rows.append(row)
					except:
						try:
							for row in CSVreader:
								Rows.append(row)
						except:
							try:
								for row in CSVreader:
									Rows.append(row)
							except:
								try:
									for row in CSVreader:
										Rows.append(row)
								except:
									try:
										for row in CSVreader:
											Rows.append(row)
									except:
										try:
											for row in CSVreader:
												Rows.append(row)
										except:
											try:
												for row in CSVreader:
													Rows.append(row)
											except:
												try:
													for row in CSVreader:
														Rows.append(row)
												except:
													try:
														for row in CSVreader:
															Rows.append(row)
													except:
														try:
															for row in CSVreader:
																Rows.append(row)
														except:
															try:
																for row in CSVreader:
																	Rows.append(row)
															except:
																try:
																	for row in CSVreader:
																		Rows.append(row)
																except:
																	try:
																		for row in CSVreader:
																			Rows.append(row)
																	except:
																		try:
																			for row in CSVreader:
																				Rows.append(row)
																		except:
																			print("ERROR")
	try:
		for row in CSVreader:
			Rows.append(row)
	except:
		try:
			for row in CSVreader:
				Rows.append(row)
		except:
			try:
				for row in CSVreader:
					Rows.append(row)
			except:
				try:
					for row in CSVreader:
						Rows.append(row)
				except:
					try:
						for row in CSVreader:
							Rows.append(row)
					except:
						try:
							for row in CSVreader:
								Rows.append(row)
						except:
							try:
								for row in CSVreader:
									Rows.append(row)
							except:
								try:
									for row in CSVreader:
										Rows.append(row)
								except:
									try:
										for row in CSVreader:
											Rows.append(row)
									except:
										try:
											for row in CSVreader:
												Rows.append(row)
										except:
											try:
												for row in CSVreader:
													Rows.append(row)
											except:
												try:
													for row in CSVreader:
														Rows.append(row)
												except:
													try:
														for row in CSVreader:
															Rows.append(row)
													except:
														try:
															for row in CSVreader:
																Rows.append(row)
														except:
															try:
																for row in CSVreader:
																	Rows.append(row)
															except:
																try:
																	for row in CSVreader:
																		Rows.append(row)
																except:
																	try:
																		for row in CSVreader:
																			Rows.append(row)
																	except:
																		try:
																			for row in CSVreader:
																				Rows.append(row)
																		except:
																			print("ERROR")

conn = sqlite3.connect('HouseDatabase.db')
c = conn.cursor()
c.execute("DROP TABLE Sales")
c.execute('''CREATE TABLE Sales
             (LatLon text, Address text, County text, Date text, SalePrice real)''')
for i in Rows:
	j = i[0]
	k = i[1]
	l = i[2]
	m = i[3]
	n = i[4]
	c.execute("INSERT INTO Sales VALUES (?,?,?,?,?)",i)