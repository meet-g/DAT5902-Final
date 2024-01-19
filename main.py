import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_unemployment_white_borough(year):
    # Function to load white employment data by year 
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    # Read file, skipping rows that are not required
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "City of London":
                continue
            if j[1] == "Westminster":
                break
            if j[20] == "!":
                pass
            else:
                percentEmployed = j[20]
                borough = j[1]
                data.append([borough,year,percentEmployed])
                # append the borough and percentage employed
            # Stop at westminister since this is the last borough
        except: 
            pass
    return data
def load_unemployment_ethnic_borough(year):
    # Function to load ethnic employment data by borough
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    # Read file, skipping rows that are not required
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "City of London":
                continue
            if j[1] == "Westminster":
                break
            if j[28] == "!":
                pass
            else:
                percentEmployed = j[28]
                borough = j[1]
                data.append([borough,year, percentEmployed])
                # append the borough and percentage employed

            # Stop at westminister since this is the last borough
        except: 
            pass
    return data

def test_load_unemployment_we_borough(year):
    # Function to read white and ethnic employment data by borough
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    # Read file, skipping rows that are not required
    data = []
    for i, j in df_2.iterrows():
        try:
            if j[1] == "City of London":
                continue
            if j[1] == "Westminster":
                break
            if j[20] == "!" or j[28] == "!":
                pass
            else:
                percentEmployedW = j[20]
                percentEmployedE = j[28]
                borough = j[1]
                data.append([borough,str(year),percentEmployedW,percentEmployedE])
                # append the borough and percentage employed
            # Stop at westminister since this is the last borough
        except: 
            pass
    return data

def load_unemployment_white_uk(year):
    # Function to load white unemployment by year - UK
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    # Read file, skipping rows that are not required
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
    # Function to load ethnic unemployment by year - UK
    employment_rate = './ea-rate-and-er-by-eg-and-nation.xls'
    df_2 = pd.read_excel(employment_rate, sheet_name=str(year), index_col=None, skiprows=2)
    # Read file, skipping rows that are not required
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

def test_plotting_ethnic_uk():
    # Plot ethnic unemployment - UK
    data = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
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

def test_plotting_white_uk():
    # Plot white unemployment - UK
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

def test_plotting_we_uk():
    # Plot both white and ethnic unemployment - UK
    dataW = []
    dataE = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataW.append(load_unemployment_white_uk(i))
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataE.append(load_unemployment_ethnic_uk(i))
        #print(data)
    year = []
    percentEmployedW = []
    percentEmployedNotUKW = [] 
    for i in dataW:
        #year.append(i[0][0])
        percentEmployedW.append(i[0][1])
        percentEmployedNotUKW.append(i[0][2])

    percentEmployedE = []
    percentEmployedNotUKE = [] 
    for i in dataE:
        year.append(i[0][0])
        percentEmployedE.append(i[0][1])
        percentEmployedNotUKE.append(i[0][2])    


    plt.xticks(rotation=90)
    plt.title("Unemployment by year")
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.plot(year, percentEmployedE, label="Ethnic Minority")
    plt.plot(year, percentEmployedNotUKE, label="Ethnic Minority [Not UK Born]")
    plt.plot(year, percentEmployedW, color="r", label="White")
    plt.plot(year, percentEmployedNotUKW, label="White [Not UK Born]")
    plt.legend()
    plt.show()

def test_plotting_wborn_uk():
    # Plot white unemployment born in the UK /  not born in the UK
    dataW = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataW.append(load_unemployment_white_uk(i))
    year = []
    percentEmployedW = []
    percentEmployedNotUKW = [] 
    for i in dataW:
        year.append(i[0][0])
        percentEmployedW.append(i[0][1])
        percentEmployedNotUKW.append(i[0][2])   


    plt.xticks(rotation=90)
    plt.plot(year, percentEmployedW, color="r", label="White")
    plt.plot(year, percentEmployedNotUKW, label="White [Not UK Born]")
    plt.title("White Unemployment by year")
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.legend()
    plt.show()

def test_plotting_eborn_uk():
    # Plot ethnic unemployment born in the UK /  not born in the UK
    dataE = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataE.append(load_unemployment_ethnic_uk(i))
        #print(data)
    year = []
    percentEmployedE = []
    percentEmployedNotUKE = [] 
    for i in dataE:
        year.append(i[0][0])
        percentEmployedE.append(i[0][1])
        percentEmployedNotUKE.append(i[0][2])    


    plt.xticks(rotation=90)
    plt.plot(year, percentEmployedE, label="Ethnic Minority")
    plt.plot(year, percentEmployedNotUKE, label="Ethnic Minority [Not UK Born]")
    plt.title("Ethnic Minority Unemployment by year")
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.legend()
    plt.show()

def test_average_unemployment_uk():
    # Compare average unemployment of ethnic individual and average unemployment of white individuals in the UK
    dataW = []
    dataE = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataW.append(load_unemployment_white_uk(i))
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataE.append(load_unemployment_ethnic_uk(i))
        #print(data)
    year = []
    percentEmployedW = []
    percentEmployedNotUKW = [] 
    for i in dataW:
        #year.append(i[0][0])
        percentEmployedW.append(i[0][1])
        percentEmployedNotUKW.append(i[0][2])

    percentEmployedE = []
    percentEmployedNotUKE = [] 
    for i in dataE:
        year.append(i[0][0])
        percentEmployedE.append(i[0][1])
        percentEmployedNotUKE.append(i[0][2])    

    averageE = np.average(percentEmployedE)
    averageW = np.average(percentEmployedW)
    return averageE, averageW

def test_corr_E():
    # Compare correlation of white unemployment born in uk / not born in uk
    dataE = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataE.append(load_unemployment_ethnic_uk(i))
        #print(data)
    year = []
    percentEmployedE = []
    percentEmployedNotUKE = [] 
    for i in dataE:
        year.append(i[0][0])
        percentEmployedE.append(i[0][1])
        percentEmployedNotUKE.append(i[0][2])    
    return np.corrcoef(percentEmployedE,percentEmployedNotUKE)

def test_corr_W():
    # Compare correlation of ethnic unemployment born in uk / not born in uk
    dataW = []
    for i in range(2005, 2023):
        if i == 2010:
            continue
        dataW.append(load_unemployment_white_uk(i))
    year = []
    percentEmployedW = []
    percentEmployedNotUKW = [] 
    for i in dataW:
        year.append(i[0][0])
        percentEmployedW.append(i[0][1])
        percentEmployedNotUKW.append(i[0][2])    
    return np.corrcoef(percentEmployedW,percentEmployedNotUKW)

def test_plot_employment_newham():
    # Plot white / ethnic unemployment in newham
    year = []
    percentEmployedE = []
    percentEmployedW = []
    data = []
    for i in range(2005,2023):
        data.append(load_unemployment_we_borough(i))
    for i in data:
        for j in i:
            if j[0] == "Newham":
                year.append(j[1])
                percentEmployedW.append(j[2])
                percentEmployedE.append(j[3])
    plt.xticks(rotation=90)
    plt.plot(year, percentEmployedE, label="Ethnic Minority")
    plt.plot(year, percentEmployedW, label="White")
    plt.title("Unemployment by year - Newham")
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.legend()
    plt.show()


def test_corr_coef_newham():
    # Obtain correlation of white unemployment vs ethnic employment - Newham
    unemploymentW = []
    unemploymentE = []
    data = []
    for i in range(2005,2023):
        data.append(load_unemployment_we_borough(i))
    for i in data:
        for j in i:
            if j[0] == "Newham":
                unemploymentW.append(j[2])
                unemploymentE.append(j[3])
    return np.corrcoef(unemploymentW,unemploymentE)
    
def test_plot_employment_merton():
    # Obtain correlation of white unemployment vs ethnic employment - Merton
    year = []
    percentEmployedE = []
    percentEmployedW = []
    data = []
    for i in range(2005,2023):
        data.append(load_unemployment_we_borough(i))
    for i in data:
        for j in i:
            if j[0] == "Merton":
                if j[2] > 50 or j[3] > 50:
                    continue
                else:
                    year.append(j[1])
                    percentEmployedW.append(j[2])
                    percentEmployedE.append(j[3])
    plt.xticks(rotation=90)
    plt.plot(year, percentEmployedE, label="Ethnic Minority")
    plt.plot(year, percentEmployedW, label="White")
    plt.title("Unemployment by year - Merton")
    plt.ylabel("Percentage")
    plt.xlabel("Year")
    plt.legend()
    plt.show()

def test_newham_merton_averages():
    validYears = [2005,2007,2008,2009,2011,2012,2013,]
    year = []
    percentEmployedEM = []
    percentEmployedWM = []
    data = []
    for i in range(2005,2023):
        data.append(load_unemployment_we_borough(i))
    for i in data:
        for j in i:
            if j[0] == "Merton" and int(j[1]) in validYears:
                if j[2] > 50 or j[3] > 50:
                    continue
                else:
                    year.append(j[1])
                    percentEmployedWM.append(j[2])
                    percentEmployedEM.append(j[3])

    # Plot white / ethnic unemployment in newham
    year = []
    percentEmployedEN = []
    percentEmployedWN = []
    data = []
    for i in range(2005,2023):
        data.append(load_unemployment_we_borough(i))
    for i in data:
        for j in i:
            if j[0] == "Newham" and int(j[1]) in validYears:
                #year.append(j[1])
                percentEmployedWN.append(j[2])
                percentEmployedEN.append(j[3])
    print(np.average(percentEmployedEM))
    print(np.average(percentEmployedEN))
    diffE = np.average(percentEmployedEN) - np.average(percentEmployedEM)
    diffW = np.average(percentEmployedWN) - np.average(percentEmployedWM)
    return diffE, diffW
