# -*- coding: utf-8 -*-
"""Data Transformation, Joins & Correlation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vs4bTJd7D0j345Elw1GJWSsgtWAh6CO4

# Data Transformation
## Contents
1. Creating the Data
"""

#Importing the library and removing the unwanted errors
import pandas as pd
import warnings
warnings.simplefilter('ignore')

"""## Creating the Data
* To understand the concepts we will work on small dataset. This time we will create our own data set.
* The simplest way to create dataset is to use list concept of python.
* Every list under the lsit wll represent every row & comma seperates the data column wise.
* Here we create two datasets:
 * GDP of countries.
 * Life expectancy of countries.
* We will then find answers to questions by analysing data.
"""

#Creating GDP Dataset
table = [

['UK', 2678454886796.7], 

['USA', 16768100000000.0], 

['China', 9240270452047.0], 

['Brazil', 2245673032353.8],

['South Africa', 366057913367.1],

['India', 25000000000.345],

['Russia', 40575984903.67]

]
headings = ['country', 'GDP (US$)']
gdp = pd.DataFrame(columns=headings, data=table)
gdp

headings = ['Country name', 'Life expectancy (years)']

table = [

['China', 75],

['Russia', 71],

['United States of America', 79],

['India', 66],

['United Kingdom', 81],

['Brazil', 58],

['South Africa', 72]

]
life_expectancy = pd.DataFrame(columns=headings, data=table)
life_expectancy

"""## Transforming Data
* We want to transform the GDP amount to the nearest millions to simplify the data readability.
* Therefore, we create function/method in python that will <b>round</b> the amount into nearest millions.
* If you dont want to return anything you can use: <pre>return None</pre>
* The built-in method <pre>round()</pre>rounds the value according to the BODMAS rules.
* We add one more method that expands the country names. 
for eg: USA-United States of America.
"""

#User defined function that convertsamount to its nearest millions. 
def roundToMillions(value):
  result = round(value / 1000000)
  return result

#Function that abrrevates the acronym.
def expandCountry(name):
  if name == "USA":
    return "United States of America"
  elif name == "UK":
    return "United Kingdom"
  else:
    return name

#Convert the currency from US$ to UKpounds.
def ustoGbp(usd):
  pounds = usd/1.564768 #aerage rate in 2013
  return pounds

"""## Applying functions
* Lets look how we can use this functions for the columns in the dataset.
* We will use the function <pre>column.apply(<i>function_name</i>)</pre> to apply the user defined function to the particular column.
"""

column = gdp['country'] #Assigning the column to the variable.
gdp['Country name'] = column.apply(expandCountry)
gdp

column = gdp['GDP (US$)']
gdp['GDP (pounds in Millions)'] = column.apply(ustoGbp).apply(roundToMillions)

#Selecting the new columns to handle data with.
gdp_in_pounds = gdp[['Country name','GDP (pounds in Millions)']]
gdp_in_pounds

"""## Joining the tables
* Here both the tables have one common column <pre>Country name</pre>
* We <b>join</b> both the tables on the country name using the <pre>merge(<i>table_1, table_2, on=column_name, how=[left,] right, center])</i>)</pre>
"""

#As we want all the columns of the left gdp_in_pounds table than we use join. 
pd.merge(gdp_in_pounds, life_expectancy, on='Country name', how='left')

# To get all the combinations we use outer Joins
df = pd.merge(gdp_in_pounds, life_expectancy, on='Country name', how='inner')

"""## Correlation between columns
* Correlation is to find the relationship between two table columns using statistical methods.
* We use scipy's spearmanr method to find the correlation between gdp and life expectancy.
"""

from scipy.stats import spearmanr
gdp_column = df['GDP (pounds in Millions)']
life_column = df['Life expectancy (years)']
(correlation, pvalue) = spearmanr(gdp_column, life_column)
print("Coorelation is", correlation)
if pvalue < 0.05:
  print("Data is statistically significant")
else: 
  print("Data is not statistically significant")

"""* This states that life expectancy is high in countries with high GDP.
* But it is not statistically signifanct because ther can be many factors affecting the life expectancy oter than GDP.
* Therefore, Always the quantitative analysis is not enough we also need qualitative analysis.
* Plotting the graph and visualize.
"""

df.plot.scatter(x="GDP (pounds in Millions)", y="Life expectancy (years)", grid=True, alpha=0.5, logx=True, figsize=(15,7))