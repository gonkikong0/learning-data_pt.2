import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
   

    # for index, column_header in enumerate(header):
    #     print (index, column_header) #Data we need Column 2,5

    dates, highs = [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    #plotting the temperatures
    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax = plt.subplots()
    ax.plot(dates,highs, c = "red")
    


    #formatting the plot
    plt.title("Daily high temperatures, July2018", fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize = 16)
    plt.tick_params(axis = 'both', which='major', labelsize = 16)

    plt.show()