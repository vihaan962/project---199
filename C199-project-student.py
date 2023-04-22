#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name")
print("Build a GUI application for data visualization of word population and on various other parameters of world population")


# # Task - Build a GUI application for data visualization of word population and on various other parameters of world population

# In[2]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map.jpg') 
#predefine code end


# In[4]:


from IPython.display import Image
Image(filename = 'Map.jpg')

from ipywidgets import widgets
from IPython.display import display, clear_output
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

graph_type = ['Choose one...', 'Bubble', 'Bar']
df = pd.read_csv('population_by_country_2020.csv')

def print_dataframe(b):
    global df
    display(df)
    head_tail_list = ['Head', 'Tail']
    xlabel_widget = widgets.Dropdown(options = df.columns)
    ylabel_widget = widgets.Dropdown(options = df.columns)
    graph_widget = widgets.Dropdown(options = graph_type)
    head_tail_widget = widgets.Dropdown(options = head_tail_list)
    row_range_widget = widgets.Dropdown(options = [10, 20, 30])
    graph = widgets.interactive(display_plot, xaxis = xlabel_widget, yaxis = ylabel_widget, head_tail = head_tail_widget, number = row_range_widget, graph_type = graph_widget)
    display(graph)
    
def display_plot(xaxis, yaxis, head_tail, number, graph_type):
    global df
    if(head_tail == 'Head'):
        dataframe = df.head(number)
    else:
        dataframe = df.tail(number)
        
    if(graph_type == 'Bubble'):
        if(dataframe[yaxis].dtypes == 'int64'):
            plt.figure(figsize = (13, 13))
            rgb = np.random.rand(3)
            plt.scatter(dataframe[xaxis], dataframe[yaxis], c = rgb, alpha = 0.4, s = dataframe[yaxis]/40000)
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)
            plt.xticks(rotation = 'vertical')
            plt.show()
        else:
            print("Bubble Graph can't be Displayed")
    elif(graph_type == 'Bar'):
        plt.figure(figsize = (13, 13))
        rgb = np.random.rand(3)
        plt.bar(dataframe[xaxis], dataframe[yaxis], color = rgb)
        plt.xlabel(xaxis)
        plt.ylabel(yaxis)
        plt.xticks(rotation = 'vertical')
        plt.show()
    else:
        print("Choose Valid Graph")

show_dataframe = widgets.Button(description = "Show Dataframe")
show_dataframe.on_click(print_dataframe)
display(show_dataframe)


# In[ ]:




