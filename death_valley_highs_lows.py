import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = "death_valley_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
   

    # for index, column_header in enumerate(header):
    #     print (index, column_header) #Data we need Column 2,5

    dates, highs, lows = [] ,[], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #plotting the temperatures (high and low)
    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax = plt.subplots()
    ax.plot(dates,highs, c = "red", alpha = 0.5)
    ax.plot(dates,lows, c = "blue", alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

    
    


    #formatting the plot
    plt.title("Daily high and low temperatures, July2018\n Death Valley, CA", fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize = 16)
    plt.tick_params(axis = 'both', which='major', labelsize = 16)

    plt.show()