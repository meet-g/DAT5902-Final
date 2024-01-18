import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_employment(year):
    employment_rate = './employment-rate-by-industry.xlsx'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    boroughs = []
    employed = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "City of London":
                continue
            percentEmployed = j[40]
            borough = j[1]
            boroughs.append(borough)
            employed.append(percentEmployed)
            # append the borough and percentage employed for the borough to two lists
            if borough == "Westminster":
                break
            # Stop at westminister since this is the last borough
        except: 
            pass
    return boroughs, employed

def load_unemployment_white_borough(year):
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "City of London":
                continue
            if j[20] == "!":
                pass
            else:
                percentEmployed = j[20]
                borough = j[1]
                data.append([borough,percentEmployed])
                # append the borough and percentage employed
            if borough == "Westminster":
                break
            # Stop at westminister since this is the last borough
        except: 
            pass
    return data

def load_unemployment_white_uk(year):
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "United Kingdom":
                percentEmployed = j[20]
                percentEmployedNotUK = j[24]
                borough = j[1]
                data.append([str(year),percentEmployed,percentEmployedNotUK])
                # append the borough and percentage employed
        except: 
            pass
    return data

def load_unemployment_ethnic_uk(year):
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "United Kingdom":
                percentEmployed = j[28]
                percentEmployedNotUK = j[32]
                borough = j[1]
                data.append([str(year),percentEmployed,percentEmployedNotUK])
                # append the borough and percentage employed
        except: 
            pass
    return data

def plotting_ethnic_uk():
    data = []
    for i in range(2005, 2023):
        data.append(load_unemployment_ethnic_uk(i))
        #print(data)
    year = []
    percentEmployed = []
    percentEmployedNotUK = [] 
    for i in data:
        year.append(i[0][0])
        percentEmployed.append(i[0][1])
        percentEmployedNotUK.append(i[0][2])
    
    plt.xticks(rotation=90)
    plt.bar(year, percentEmployed)
    plt.show()

def plotting_white_uk():
    data = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        data.append(load_unemployment_white_uk(i))
        #print(data)
    year = []
    percentEmployed = []
    percentEmployedNotUK = [] 
    for i in data:
        year.append(i[0][0])
        percentEmployed.append(i[0][1])
        percentEmployedNotUK.append(i[0][2])
    
    plt.xticks(rotation=90)
    plt.bar(year, percentEmployed)
    plt.show()


plotting_white_uk()


