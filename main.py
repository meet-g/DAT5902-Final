import numpy as np
import pandas
import matplotlib.pyplot as plt

df = pandas.ExcelFile("./businessdemographyexceltables2022.xlsx")
print(df.sheet_names)


seventeenBirths  = []
eighteenBirths  = []
nineteenBirths  = []
twentyBirths  = []
twentyoneBirths  = []
twentytwoBirths  = []

sheetOne = pandas.read_excel(df, sheet_name='Table 1.1a')
sheetTwo = pandas.read_excel(df, sheet_name='Table 1.1b')
sheetThree = pandas.read_excel(df, sheet_name='Table 1.1c')
sheetFour = pandas.read_excel(df, sheet_name='Table 1.1d')
for i in sheetOne.values[3:7]:
    seventeenBirths.append(i[2])
    eighteenBirths.append(i[3])

for i in sheetTwo.values[3:7]:
    nineteenBirths.append(i[2])

for i in sheetThree.values[3:7]:
    twentyBirths.append(i[2])

for i in sheetFour.values[3:7]:
    twentyoneBirths.append(i[2])
    twentytwoBirths.append(i[3])

sheetFive = pandas.read_excel(df, sheet_name='Table 2.1a')
sheetSix = pandas.read_excel(df, sheet_name='Table 2.1b')
sheetSeven = pandas.read_excel(df, sheet_name='Table 2.1c')
sheetEight = pandas.read_excel(df, sheet_name='Table 2.1d')

for i in sheetFive.values[3:7]:
    seventeenBirths.append(i[2])
    eighteenBirths.append(i[3])

for i in sheetSix.values[3:7]:
    nineteenBirths.append(i[2])

for i in sheetSeven.values[3:7]:
    twentyBirths.append(i[2])

for i in sheetEight.values[3:7]:
    twentyoneBirths.append(i[2])
    twentytwoBirths.append(i[3])

print(seventeenBirths)
print(eighteenBirths)