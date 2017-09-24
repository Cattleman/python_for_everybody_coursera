# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:22:53 2016
code from: http://www.datasciencecentral.com/group/tutorials/forum/topics/cheat-sheet-data-visualisation-in-python
use anaconda2 with spyder IDE
@author: Hensel
"""

print "hello world."

#to do data vis stuff need to import the following:
import matplotlib.pyplot as plt
import pandas as pd

#point at excel file
df=pd.read_excel("D:first.xlsx","Sheet1")

#bar chart

#groupby variable must be same as column head in xslx worksheet (case sensitive)
var=df.groupby('month').Revenue.sum()
#grouped sum of sales by month
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Month')
ax1.set_ylabel('Revenue')
ax1.set_title("Revenue by Month")
var.plot(kind='bar')

#Line Chart
var=df.groupby('month').Revenue.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('month')
ax1.set_ylabel('Revenue by month')
ax1.set_title("Revenue  over time")

var.plot(kind='line')

#Stacked column Chart

var = df.groupby(['month','Revenue']).Revenue.sum()
var.unstack().plot(kind='bar',stacked=True, color=['red','blue'],grid=False)

#scatter plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['month'],df['Revenue'])
plt.show()

#bubble plot

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['month'],df['Revenue'], s=df['profit'])
plt.show()

#Pie Charts! woot woot!
var = df.groupby(['Revenue']).sum().stack()
temp=var.unstack()
type(temp)
x_list =temp['month']
label_list = temp.index
#the pie chart is oval by defalt. to make it a circle use plt.axis("equal")
plt.axis("equal")
plt.pie(x_list,labels=label_list,autopct="%1.1f%%")
plt.title("Revenue by month")
plt.show()

#heat map wootz!

import numpy as np
data = np.random.rand(4,2)
rows = list('1234') #rows categories 
columns = list('MF') #column categories
fig,ax=plt.subplots()
ax.pcolor(data,cmap=plt.cm.Reds,edgecolors='k')
ax.set_xticks(np.arange(0,2)+0.5)
ax.set_yticks(np.arange(0,4)+0.5)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_xticklabels(columns,minor=False,fontsize=20)
ax.set_yticklabels(rows,minor=False,fontsize=20)
plt.show()