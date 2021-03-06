# -*- coding: utf-8 -*-
"""pandasIntroduction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHKWN5zMSuT7eMExX0YVH8xVvs8Lmuof

### Introduction to pandas:
<ul>
<li>This notebook introduces one to the data handling library of python i.e <b>pandas.</b></li>
<li>The dataset that is used is provided by <b>WHO</b> to monitor <b>TB deaths in BRICS</b> countries.</li>
<li>This notebook has notes in form of comments written inside code cells</li>
</ul> 
<h4><b>Author:</b> Vishva Patel</h4>
<h4><b>Github Repository:</b> Data Visualization with python<h4>
"""

import pandas as pd #This is python's builtin library to work with data analysis.

#Loading the dataset. Don't forget to upload the file. 
dataset = pd.read_excel('WHO POP TB all.xls');
dataset #printing the dataset.

#Accessing a column from a dataset
dataset['TB deaths']

#Calculations with columns
tbDeaths = dataset['TB deaths']
tbDeaths.sum() #calculates the total deaths.

#Calculating the min and max deaths
print("Minimum deaths")
tbDeaths.min() #calculating the minimum.

print("Maximum deaths")
tbDeaths.max() #calculating the maximum of the column.

#Calculating the average deaths in all the countries
tbDeaths.sum() / 194

#one can also use mean() method
tbDeaths.mean()

#Calculating the median
tbDeaths.median()

#Sorting the values in the columns 
#Python has a built-in method wichtakes a column as an argument and retunrs a sorted dataframe.
dataset.sort_values('TB deaths')
#Make sure that this does not change the actual data.

#Sorting does not only happens with numbers, it can also be used with string datatypes.
#sort_values() for a string sorts in alphabetical order.
dataset.sort_values('Country')

#selecting just a specific columns 
dataset[['Country', 'Population (1000s)']]

#Adding a new column
#We will add a column that will display the difference from average of the population for each country.
dataset['Diff_from_avg'] = dataset['Population (1000s)'] - dataset['Population (1000s)'].mean() 
dataset['Diff_from_avg']