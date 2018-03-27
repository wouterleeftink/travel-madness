# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:28:34 2018

@author: wle
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fiveseven = pd.read_csv('accidents_2005_to_2007.csv')
nineeleven = pd.read_csv('accidents_2009_to_2011.csv')
twelvefourteen = pd.read_csv('accidents_2012_to_2014.csv')
aadf = pd.read_csv('ukTrafficAADF.csv')



frames = [fiveseven, nineeleven, twelvefourteen]
accidents = pd.concat(frames)

road_types = accidents.groupby('Road_Type')['Accident_Index'].nunique().sort_values(ascending = False)
road_types.plot('bar')

motorway_accidents = accidents[accidents['1st_Road_Class'] == 1]
motorway = motorway_accidents.groupby('1st_Road_Number')['Accident_Index'].nunique().sort_values(ascending = False)
motorway = motorway.rename(lambda x: 'M'+ str(x))

aroad_accidents = accidents[accidents['1st_Road_Class'] == 2]
aroad_accidents2 = accidents[accidents['1st_Road_Class'] == 3]
aroad_accidents = [aroad_accidents, aroad_accidents2]
aroad_accidents = pd.concat(aroad_accidents)
aroad = aroad_accidents.groupby('1st_Road_Number')['Accident_Index'].nunique().sort_values(ascending = False)
aroad = aroad.rename(lambda x: 'A' + str(x))

broad_accidents = accidents[accidents['1st_Road_Class'] == 4]
broad = broad_accidents.groupby('1st_Road_Number')['Accident_Index'].nunique().sort_values(ascending = False)
broad = broad.rename(lambda x: 'B' + str(x))

all_roads = [motorway, aroad, broad]
all_roads = pd.concat(all_roads).sort_values(ascending = False)

top_10_motorway = motorway.head(10)
top_10_motorway.plot('bar')

top_10_aroad = aroad.head(10)
top_10_aroad.plot('bar')

top_10_broad = broad.head(10)
top_10_broad.plot('bar')

top_10_allroad = all_roads.head(10)
top_10_allroad.plot('bar')

print(all_roads.index)
columns = ['Road', 'PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 'LightGoodsVehicles', 'AllHGVs', 'AllMotorVehicles', 'Accidents']
roadframe = pd.DataFrame(columns = columns)
for road in all_roads.index:
    road_matrix = aadf[aadf['Road'] == road]
    if not road_matrix.empty and not np.isnan(all_roads[road]):
        pedals = road_matrix['PedalCycles'].mean()
        motor = road_matrix['Motorcycles'].mean()
        cars = road_matrix['CarsTaxis'].mean()
        buses = road_matrix['BusesCoaches'].mean()
        lightgoods = road_matrix['LightGoodsVehicles'].mean()
        heavygoods = road_matrix['AllHGVs'].mean()
        allmotorvehicles = road_matrix['AllMotorVehicles'].mean()
        roadframe = roadframe.append({'Road': road,
                                      'PedalCycles': pedals, 
                                      'Motorcycles': motor, 
                                      'CarsTaxis': cars,
                                      'BusesCoaches': buses,
                                      'LightGoodsVehicles': lightgoods,
                                      'AllHGVs': heavygoods,
                                      'AllMotorVehicles': allmotorvehicles,
                                      'Accidents': float(all_roads[road])}, ignore_index = True)
correlation = roadframe.corr()    
