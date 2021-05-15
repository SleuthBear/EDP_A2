import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.style.use('ggplot')
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

#melbourne.plot.scatter("Power", "House_Price_Index")
#melbourne.plot.scatter("Power", "Wage_Index")
#plt.scatter(x=melbourne.index, y=melbourne.Power)
#plt.scatter(x=melbourne.index, y=melbourne.House_Price_Index)
#plt.show()

# Regression line calculation
def create_regression(df):    

    fig, ax = plt.subplots(2, 2)


    # Get training set for House Prices
    Wage_Train = df.Wage_Index.loc["03":"20"].to_numpy()
    Wage_Train = Wage_Train.reshape(-1, 1)
    HPI_Train = df.House_Price_Index.loc["03":"20"].to_numpy()
    HPI_Train = HPI_Train.reshape(-1, 1)
    
    # Get regression line
    regression_HPI = LinearRegression()
    regression_HPI.fit(Wage_Train, HPI_Train)
    reg_x = np.array([[60, 150]])
    reg_x = reg_x.reshape(-1, 1)
    reg_y = regression_HPI.predict(reg_x)


    R2 = regression_HPI.score(Wage_Train, HPI_Train)
    grad = (reg_y[1]-reg_y[0])/(reg_x[1]-reg_x[0])
    ax[0,0].set_title(f"Hourly Pay to House Prices - R^2 = {R2} - Gradient = {grad}")
    ax[0,0].scatter(x=df.Wage_Index, y=df.House_Price_Index)
    ax[0,0].plot(reg_x, reg_y)
    ax[0,0].set_xlabel("Hourly Pay")
    ax[0,0].set_ylabel("House Prices")

    # Plotting residuals for HPI
    res_reg = regression_HPI.predict(Wage_Train)
    residuals = HPI_Train - res_reg
    ax[0,1].set_title("Hourly Pay to House Prices Residuals")
    ax[0,1].scatter(Wage_Train, residuals)
    ax[0,1].set_xlabel("Hourly Pay")
    ax[0,1].set_ylabel("House Price Residuals")

    # Get Training set for CPI
    Wage_Train = df.Wage_Index.loc["98":"20"].to_numpy()
    Wage_Train = Wage_Train.reshape(-1, 1)
    CPI_Train = df.CPI_Index.loc["98":"20"].to_numpy()
    CPI_Train = CPI_Train.reshape(-1, 1)

    # Get regression line
    regression_CPI = LinearRegression()
    regression_CPI.fit(Wage_Train, CPI_Train)
    reg_x = np.array([[60, 150]])
    reg_x = reg_x.reshape(-1, 1)
    reg_y = regression_CPI.predict(reg_x)

    R2 = regression_CPI.score(Wage_Train, CPI_Train)
    grad = (reg_y[1]-reg_y[0])/(reg_x[1]-reg_x[0])
    ax[1,0].set_title(f"Hourly Pay to CPI - R^2 = {R2} - Gradient = {grad}")
    ax[1,0].scatter(x=df.Wage_Index, y=df.CPI_Index)
    ax[1,0].set_xlabel("Hourly Pay")
    ax[1,0].set_ylabel("CPI")
    ax[1,0].plot(reg_x, reg_y)

    # Plotting residuals for CPI
    res_reg = regression_CPI.predict(Wage_Train)
    residuals = CPI_Train - res_reg
    ax[1,1].set_title("Hourly Pay to CPI Residuals")
    ax[1,1].set_xlabel("Hourly Pay")
    ax[1,1].set_ylabel("CPI Residuals")
    ax[1,1].scatter(Wage_Train, residuals)

    fig.tight_layout(pad=3.0)
    fig.set_size_inches(15, 10)
    plt.show()

create_regression(capitals_avg)
