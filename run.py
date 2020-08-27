# This is my first trying code
import pandas 
import matplotlib.pyplot as plt

filename="data.csv"
data=pandas.read_csv("data.csv")
print(data)

year=data.Year
print(year)
print(year[0])

temperature=data.Value
print(temperature[0])

print(year[1])
print (temperature[1])

print(year[2])
print(temperature[2])

print(year[137])
print(temperature[137])

print(year[138])
print(temperature[138])

print(year[139])
print(temperature[139])

plt.plot(year,temperature)

plt.xlabel("year")
plt.ylabel("temperature")
plt.title("temperature vs. year")

plt.show()