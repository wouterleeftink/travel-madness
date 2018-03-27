# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:28:34 2018

@author: wle
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mapsplotlib import mapsplot as mplt
import statsmodels.api as sm

mplt.register_api_key('AIzaSyAwCqLkvYkuEYTNgMFTPaM9Ldq7ipO-jco')

fiveseven = pd.read_csv('accidents_2005_to_2007.csv')
nineeleven = pd.read_csv('accidents_2009_to_2011.csv')
twelvefourteen = pd.read_csv('accidents_2012_to_2014.csv')

frames = [fiveseven, nineeleven, twelvefourteen]
accidents = pd.concat(frames)
small_frames = [nineeleven, twelvefourteen]
small_accidents = pd.concat(small_frames)

road_types = accidents.groupby('Road_Type')['Accident_Index'].nunique().sort_values(ascending = False)
road_types.plot('bar')

small_accidents['Date'] = pd.to_datetime(small_accidents['Date'])
day_accidents = small_accidents.groupby('Date')['Accident_Index'].nunique()

month_accidents2 = day_accidents.groupby(pd.Grouper(freq = 'M')).sum()

day_accidents.plot()
month_accidents2.plot()

pd.plotting.autocorrelation_plot(month_accidents2)


month_accidents2 = month_accidents2.astype(np.float)
res = sm.tsa.ARIMA(month_accidents2, order = (15,0,0)).fit()
#print(res.summary())

#residuals3 = pd.DataFrame(res.resid)
#residuals3.plot()
#plt.show()
#residuals3.plot(kind='kde')
#plt.show()
#print(residuals3.describe())
res.plot_predict(start='02-28-2011', end='12-31-2018')