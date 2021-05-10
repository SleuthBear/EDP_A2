import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

CPI = pd.read_csv("data sources/USED/CPI_melbourne.csv")
WAGES = pd.read_csv("data sources/USED/wage_index_melbourne.csv")
HOUSEPRICES = pd.read_csv("data sources/USED/houseprices_index_melbourne.csv")
   
CPI["Date"] = CPI["Date"].str[-2:]    
WAGES["Date"] = WAGES["Date"].str[-2:]
HOUSEPRICES["Date"] = HOUSEPRICES["Date"].str[-2:]                                
CPI_GROUP = CPI.groupby(by="Date", sort=False).mean()
WAGE_GROUP = WAGES.groupby(by="Date", sort=False).mean()
HOUSEPRICES_GROUP = HOUSEPRICES.groupby(by="Date", sort=False).mean()
melbourne = CPI_GROUP
melbourne = melbourne.join(WAGE_GROUP).join(HOUSEPRICES_GROUP)

melbourne.plot.scatter(x="Wage_Index", y="CPI_Index")
melbourne.plot.scatter(x="Wage_Index", y="House_Price_Index")
plt.show()