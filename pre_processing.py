import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


def create_dataframe(city):

    CPI = pd.read_csv(f"data sources/CITIES/{city}/CPI_{city}.csv")
    WAGES = pd.read_csv(f"data sources/CITIES/{city}/WI_{city}.csv")
    HOUSEPRICES = pd.read_csv(f"data sources/CITIES/{city}/HPI_{city}.csv")
   
    CPI["Date"] = CPI["Date"].str[-2:]    
    WAGES["Date"] = WAGES["Date"].str[-2:]
    HOUSEPRICES["Date"] = HOUSEPRICES["Date"].str[-2:]                                
    CPI_GROUP = CPI.groupby(by="Date", sort=False).mean()
    WAGE_GROUP = WAGES.groupby(by="Date", sort=False).mean()
    HOUSEPRICES_GROUP = HOUSEPRICES.groupby(by="Date", sort=False).mean()
    frame = CPI_GROUP
    frame = frame.join(WAGE_GROUP).join(HOUSEPRICES_GROUP)
    
    if city == "melbourne":
        POWER = pd.read_csv(f"data sources/CITIES/{city}/Power_{city}.csv")
        POWER["Date"] = POWER["Date"].str[2:4]  
        POWER_GROUP = POWER.groupby(by="Date", sort=False).mean()  
        frame = frame.join(POWER_GROUP)

    #frame.plot.scatter(x="Wage_Index", y="CPI_Index")
    #frame.plot.scatter(x="Wage_Index", y="House_Price_Index")
    #plt.show()
    return frame

melbourne = create_dataframe("melbourne")
perth = create_dataframe("perth")
adelaide = create_dataframe("adelaide")
hobart = create_dataframe("hobart")
canberra = create_dataframe("canberra")
brisbane = create_dataframe("brisbane")
darwin = create_dataframe("darwin")
sydney = create_dataframe("sydney")
capitals_avg = create_dataframe("capitals_avg")
