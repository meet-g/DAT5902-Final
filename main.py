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

