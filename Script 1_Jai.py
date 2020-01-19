# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

%reset -f
import pandas as pd
import numpy as np
import os

os.chdir(r'/home/jai/Downloads/Rapido Assignment')

dt = pd.read_excel('Rapido Data Analyst Assignment DataSet.xlsx')
#%%
import datetime
def convert(x):
    return datetime.datetime.fromtimestamp(x/1e3)

dt['timestamp'] = dt['timestamp'].apply(lambda x: convert(x))
dt['date'] =dt['timestamp'].apply(lambda x :x.date())
dt['time'] =dt['timestamp'].apply(lambda x :x.time())

lst =[datetime.time(0, 0, 0),datetime.time(5, 0, 0),datetime.time(7, 30, 0),
      datetime.time(10, 30, 0),datetime.time(12, 0, 0),datetime.time(15, 0, 0),
      datetime.time(17, 0, 0),datetime.time(20, 0, 0),datetime.time(21, 30, 0)]

def TimeBin(x):
    if (x>datetime.time(0, 0, 0))&(x<=datetime.time(5, 0, 0)):
        return '01.Night (12 AM - 05 AM)'
    elif (x>datetime.time(5, 0, 0))&(x<=datetime.time(7, 30, 0)):
        return '02.Early Morning (05 AM - 07:30AM)'
    elif (x>datetime.time(7,30, 0))&(x<=datetime.time(10, 30, 0)):
        return '03.Office Start (07:30 AM - 10:30 AM)'
    elif (x>datetime.time(10,30, 0))&(x<=datetime.time(12, 30, 0)):
        return '04.Working Hours - Morning (10:30 AM - 12:30 PM)'
    elif (x>datetime.time(12,30, 0))&(x<=datetime.time(15, 00, 0)):
        return '05.Lunch(12:30 PM - 03:00 PM)'
    elif (x>datetime.time(15,00, 0))&(x<=datetime.time(17, 30, 0)):
        return '06.Working Hours - Evening(03:00 PM - 05:30 PM)'
    elif (x>datetime.time(17,30, 0))&(x<=datetime.time(20, 30, 0)):
        return '07.Office Return(05:30 PM - 08:30 PM)'
    elif (x>datetime.time(20,30, 0))&(x<=datetime.time(22, 00, 0)):
        return '08.Late Returns(08:30 PM - 10:00 PM)' 
    else:
        return '09.Late Night(10:00 PM - !2:00 AM)'
    
dt['timebin'] = dt['time'].apply(lambda x: TimeBin(x))

#%%
#data = dt.loc[dt['date']==,'timebin'].value_counts().reset_index().sort_values(by = ['index'])
data = dt.loc[:,'timebin'].value_counts().reset_index().sort_values(by = ['index']).reset_index(drop = True)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(data['index'],data['timebin'])

plt.show()

#%%
plot_data = pd.pivot_table(dt[['trip_id','date','timebin']],values = 'trip_id',
                                                columns = 'date',
                                                index = 'timebin',
                                                aggfunc = 'count').reset_index()

plot_data.columns = ['timebin','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']
#%%
