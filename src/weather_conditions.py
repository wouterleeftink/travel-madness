# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:48:06 2018

@author: wle
"""

import pandas as pd

fiveseven = pd.read_csv('accidents_2005_to_2007.csv')
nineeleven = pd.read_csv('accidents_2009_to_2011.csv')
twelvefourteen = pd.read_csv('accidents_2012_to_2014.csv')

frames = [fiveseven, nineeleven, twelvefourteen]
accidents = pd.concat(frames)

weather_conditions = accidents.groupby('Weather_Conditions')['Accident_Index'].nunique().sort_values(ascending = False)
surface_conditions = accidents.groupby('Road_Surface_Conditions')['Accident_Index'].nunique().sort_values(ascending = False)
light_conditions = accidents.groupby('Light_Conditions')['Accident_Index'].nunique().sort_values(ascending = False)

weather_light_conditions = accidents.groupby(['Weather_Conditions', 'Light_Conditions'])['Accident_Index'].nunique().sort_values(ascending = False)
top_9_weather_light_conditions = weather_light_conditions.head(9)
weather_surface_conditions = accidents.groupby(['Weather_Conditions', 'Road_Surface_Conditions'])['Accident_Index'].nunique().sort_values(ascending = False)
top_9_weather_surface_conditions = weather_surface_conditions.head(9)
surface_light_conditions = accidents.groupby(['Road_Surface_Conditions', 'Light_Conditions'])['Accident_Index'].nunique().sort_values(ascending = False)
top_9_surface_light_conditions = surface_light_conditions.head(9)

all_conditions = accidents.groupby(['Weather_Conditions', 'Light_Conditions', 'Road_Surface_Conditions'])['Accident_Index'].nunique().sort_values(ascending = False)
top_9_all_conditions = all_conditions.head(9)

print(weather_conditions)
print(surface_conditions)
print(light_conditions)

print(weather_light_conditions)
print(weather_surface_conditions)
print(surface_light_conditions)

print(all_conditions)

weather_conditions.plot('bar', title = 'Number of accidents per weather condition')
surface_conditions.plot('bar', title = 'Number of accidents per road surface condition')
light_conditions.plot('bar', title = 'Number of accidents per light condition')

top_9_weather_light_conditions.plot('bar', title = 'Top 9 weather + light conditions for number of accidents')
top_9_weather_surface_conditions.plot('bar', title = 'Top 9 weather + surface conditions for number of accidents')
top_9_surface_light_conditions.plot('bar', title = 'Top 9 surface +light conditions for number of accidents')

top_9_all_conditions.plot('bar', title = 'Top 9 combined conditions for number of accidents')