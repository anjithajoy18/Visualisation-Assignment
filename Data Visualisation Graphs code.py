# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:42:32 2022

@author: Anjikutty
"""

#Importing needed packages
import matplotlib.pyplot as plt
import pandas as pd

def lineplotOfGasEmission():     

     #Plotting line plots for the gas emission change    years=['1999','2008','2012']
     plt.figure(figsize=(14,9))
     #Iterating the years
     for i in range(0,len(years)): 
         plt.plot(gasEmission['Country Code'],gasEmission[years[i]],label=years[i])
         plt.scatter(gasEmission['Country Code'],gasEmission[years[i]],color='black')
     plt.xticks(rotation=270)
     plt.title("Total green house gas Emission percenatge change in 1999-2012",color='red',size=25)
     plt.xlabel('Countries-->')
     plt.ylabel('Percentage of gas emission change-->')
     plt.legend()
     plt.savefig('linelot.png',dpi=200)
     line=plt.show()
     
     return line

#Creating a box plot to analyze the average of gas emission change in each year
def MedianofGasEmission():

    #Plotting Box plot for finding the average of change in the gas emission percentage
    plt.figure(figsize=(14,9))
    plt.boxplot([gasEmission['2000'],gasEmission['2002'],gasEmission['2004'],gasEmission['2006']],labels=['2000','2002','2004','2006'])
    plt.title('Analyzis of the average gas emission change in each year',color='red',size=25)
    plt.xlabel('years-->')
    plt.ylabel('gas emission change-->')
    plt.legend()
    plt.savefig('boxplot.png',dpi=200)
    box=plt.show()
    return box

#Creating a bar diagram to analyze the percentage of gas emission change
def bardiagramAnalysis():
    
    #Plotting bar diagram for the gas emission change
    plt.figure(figsize=(14,9))
    colr=['violet','indigo','blue','green','yellow','orange','red']
    plt.bar(gasEmission['Country Code'],gasEmission['1999'],width=0.35, color=colr,edgecolor='black')
    plt.title('The gas emission change in the year of 1999',color='red',size=25)
    plt.xlabel('Countries-->')
    plt.ylabel('gas emission percentage change-->')
    plt.legend()
    plt.savefig('bardiagram.png',dpi=200)
    bar=plt.show()
    return bar


#Reading csv Files
gasEmission=pd.read_csv("Greenhouse Data.csv")
years=['1999','2012']

#Calling the functions
lineplotOfGasEmission()
MedianofGasEmission()
bardiagramAnalysis()