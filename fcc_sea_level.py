import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file

    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df["Year"], df['CSIRO Adjusted Sea Level'])
  

    # Create first line of best fit
   
    
    
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = pd.Series([i for i in range(1880,2050)])
    y = x*slope+intercept

    ax2 =plt.plot(x, intercept + slope*x, 'r', label='fitted line')
    # Create second line of best fit
    df_2020 = df.copy()
    df_2020= df[df_2020["Year"]>=2000]
    
    slope, intercept, r_value, p_value, std_err = linregress(df_2020["Year"], df_2020["CSIRO Adjusted Sea Level"])
    x = pd.Series([i for i in range(2000,2050)]) 
    y = x*slope+intercept
    
    ax3 = plt.plot(x, intercept + slope*x, 'r', label='fitted line 2')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
