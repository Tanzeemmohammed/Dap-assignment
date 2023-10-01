import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("airline-safety.csv")
dataframe = pd.DataFrame(data)
dfh = dataframe.head(20)
dfh.plot(x="airline", y="incidents_85_99", kind="bar", title="Airline accidents")
plt.show()