import pandas as pd
import re

def extract_cpidata(filename) :
    cpi = pd.read_csv(filename, encoding = 'ISO-8859-1')
    
    for date in cpi['Date'] :
        if "Jun" not in date:
            index = cpi.index[cpi['Date'] == date].tolist()
            cpi = cpi.drop(index)
    
    cpi = cpi.reset_index(drop=True)

    cpi.drop(cpi.index[0:49],0,inplace=True)
    
    return cpi
    
cpi_adelaide = extract_cpidata("CPI_adelaide.csv")
cpi_brisbane = extract_cpidata("CPI_brisbane.csv")
cpi_canberra = extract_cpidata("CPI_canberra.csv")
cpi_avg = extract_cpidata("CPI_capitals_avg.csv")
cpi_darwin = extract_cpidata("CPI_darwin.csv")
cpi_hobart = extract_cpidata("CPI_hobart.csv")
cpi_melbourne = extract_cpidata("CPI_melbourne.csv")
cpi_perth = extract_cpidata("CPI_perth.csv")
cpi_sydney = extract_cpidata("CPI_sydney.csv")

wi_adelaide = pd.read_csv("WI_adelaide.csv", encoding = 'ISO-8859-1')
wi_brisbane = pd.read_csv("WI_brisbane.csv", encoding = 'ISO-8859-1')
wi_canberra = pd.read_csv("WI_canberra.csv", encoding = 'ISO-8859-1')
wi_avg = pd.read_csv("WI_capitals_avg.csv", encoding = 'ISO-8859-1')
wi_darwin = pd.read_csv("WI_darwin.csv", encoding = 'ISO-8859-1')
wi_hobart = pd.read_csv("WI_hobart.csv", encoding = 'ISO-8859-1')
wi_melbourne = pd.read_csv("WI_melbourne.csv", encoding = 'ISO-8859-1')
wi_perth = pd.read_csv("WI_perth.csv", encoding = 'ISO-8859-1')
wi_sydney = pd.read_csv("WI_sydney.csv", encoding = 'ISO-8859-1')

%matplotlib inline
import matplotlib.pyplot as plt

plt.plot( wi_adelaide['Wage_Index'], cpi_adelaide['CPI_Index'], color='red', label='Adelaide')
plt.plot( wi_brisbane['Wage_Index'], cpi_brisbane['CPI_Index'], color='blue', label='brisbane')
plt.plot( wi_canberra['Wage_Index'], cpi_canberra['CPI_Index'], color='green', label='canberra')
plt.plot( wi_avg['Wage_Index'], cpi_avg['CPI_Index'], color='black', label='average')
plt.plot( wi_darwin['Wage_Index'], cpi_darwin['CPI_Index'], color='cyan', label='darwin')
plt.plot( wi_hobart['Wage_Index'], cpi_hobart['CPI_Index'], color='yellow', label='hobart')
plt.plot( wi_melbourne['Wage_Index'], cpi_melbourne['CPI_Index'], color='gray', label='melbourne')
plt.plot( wi_perth['Wage_Index'], cpi_perth['CPI_Index'], color='orange', label='perth')
plt.plot( wi_sydney['Wage_Index'], cpi_sydney['CPI_Index'], color='magenta', label='sydney')
plt.xlabel("Wage Index")
plt.ylabel("CPI Index")
plt.grid(True)
plt.legend()

## Compare Wage Index vs. CPI Index between only melbounre and average of capitals
plt.plot( wi_melbourne['Wage_Index'], cpi_melbourne['CPI_Index'], color='red', label='melbourne')
plt.plot( wi_avg['Wage_Index'], cpi_avg['CPI_Index'], color='blue', label='average')
plt.xlabel("Wage Index")
plt.ylabel("CPI Index")
plt.grid(True)
plt.legend()

## Wage Index vs. House Price Index between Melbourne and captials average
def extract_hpidata(filename) :
    hpi = pd.read_csv(filename, encoding = 'ISO-8859-1')
    
    for date in hpi['Date'] :
        if "Jun" not in date:
            index = hpi.index[hpi['Date'] == date].tolist()
            hpi = hpi.drop(index)
    
    hpi = hpi.reset_index(drop=True)
    
    return hpi

hpi_melbourne = extract_hpidata("HPI_melbourne.csv")
hpi_avg = extract_hpidata("HPI_capitals_avg.csv")

wi_melbourne = wi_melbourne.iloc[6:]
wi_avg = wi_avg.iloc[6:]

plt.plot( wi_melbourne['Wage_Index'], hpi_melbourne['House_Price_Index'], color='red', label='melbourne')
plt.plot( wi_avg['Wage_Index'], hpi_avg['House_Price_Index'], color='blue', label='average')
plt.xlabel("Wage Index")
plt.ylabel("House Price Index")
plt.grid(True)
plt.legend()
