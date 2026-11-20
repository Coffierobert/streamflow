
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file
data = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    dtype=str,
    skip_header=1
)


x = np.array(data[:, 0], dtype='datetime64[m]')

y_1 = data[:, 1].astype(float)  # Site 10163000
y_2 = data[:, 2].astype(float)  # Site 10155200
y_3 = data[:, 3].astype(float)  # Site 10155500
y_4 = data[:, 4].astype(float)  # Site 10154200
y_5 = data[:, 5].astype(float)  # Site 10155000

# Check the first few values
print("Dates:", x[:5])
print("Site 10163000:", y_1[:5])
print("Site 10155200:", y_2[:5])
print("Site 10155500:", y_3[:5])
print("Site 10154200:", y_4[:5])
print("Site 10155000:", y_5[:5])

"""### Graphing the Data

Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.
"""

# Create the graph
plt.figure(figsize=(10, 6))


plt.plot(x, y_1, label='10163000')
plt.plot(x, y_2, label='10155200')
plt.plot(x, y_3, label='10155500')
plt.plot(x, y_4, label='10154200')
plt.plot(x, y_5, label='10155000')


plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')


plt.legend(title='Site Numbers')
plt.grid(True)


plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter('%Y-%m-%d')
)

plt.gca().xaxis.set_major_locator(
    mdates.DayLocator(interval=4)
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

