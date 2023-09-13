import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

conn = sqlite3.connect("climate.db")
cursor = conn.cursor()
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")

data = cursor.fetchall()
for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

conn.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.savefig("co2_temp_1.png") # had to swap this line above .show() for it to work
plt.show()

