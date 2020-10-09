#!/usr/bin/env python
# coding: utf-8

# # Matplotlib LIBRARY
# It is used to visualize the data. Data visualization is presentation of data in graphical form. This can be done by **matplotlib** library of python.

# By using matplotlib library we can plot 2D graphs and these are- 
# **(1)** Bar Graph,
# **(2)** Histograms,
# **(3)** Sactter Plot,
# **(4)** Pie Plot,
# **(5)** Hexagonal Bin Plot,
# **(6)** Area Plot

# In[2]:


import matplotlib


# In[3]:


from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.show()


# In[4]:


from matplotlib import pyplot as plt
plt.plot([11,3,56],[32,54,35])
plt.show()


# **Now, we add x-axis and y-axis labels and also title of graph**

# In[6]:


from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,6])                #x=[1,2,3]
plt.title("Graph representation")        #y=[4,5,6]
plt.xlabel("X-axis")                     #plt.plot(x,y)  we use these lines instead od 2nd line of this section both are same
plt.ylabel("Y-axis")
plt.show()


# **We can accumulate some more thngs into our graph to give more information. Here we give color to our plot lines and give label to each line.**

# In[18]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")

x1=[10,23,55]
y1=[1,4,8]

x2=[24,46,69]
y2=[36,4,23]

plt.plot(x1,y1,'r',label='1st line',linewidth=4)
plt.plot(x2,y2,'g',label='2nd line',linewidth=4)

plt.title("Graph Representation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.show()


# In[19]:


from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")

x1=[10,23,55]
y1=[1,4,8]

x2=[24,46,69]
y2=[36,4,23]

plt.plot(x1,y1,'r',label='1st line',linewidth=4)
plt.plot(x2,y2,'g',label='2nd line',linewidth=4)

plt.title("Graph Representation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.grid(True,color='K')

plt.show()


# **These are some basic things that a graph must have while we plot it. It gives all athe information related to graph.**

# **Now we plot various types of graphs using matplotlib**

# # (1) Bar Graph 

# In[22]:


import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="1st one", color='r')
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="2nd one", color='g')
plt.legend()

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bar Graph")

plt.show()


# #  (2) Histogram

# In[28]:


import matplotlib.pyplot as plt

ages=[22,55,62,45,21,33,43,5,55,62,6,25,88,35,85,35,65,73,123,4,56,4,132,453,55,144,53,5,23,2,111,43]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]

plt.hist(ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram")

plt.show()


# #  (3) Scatter plot

# In[31]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label="skitscat", color='k', marker="o")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sactter plot")
plt.legend()

plt.grid(True,color='K')
plt.show()


# #  (4) Area Plot
# **Area plot is also known as Stake plot**

# In[33]:


import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sleep=[7,8,6,11,7]
eat=[2,3,4,3,2]
work=[7,8,7,2,2]
play=[8,5,7,8,13]

plt.plot([],[],color='m',label="sleep",linewidth=5)
plt.plot([],[],color='c',label="eat",linewidth=5)
plt.plot([],[],color='r',label="work",linewidth=5)
plt.plot([],[],color='k',label="play",linewidth=5)

plt.stackplot(days, sleep, eat, work, play, colors=['m','c','r','k'])

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Area plot / Stack Plot")
plt.legend()

plt.show()


# #  (5) Pie Chart

# In[40]:


import matplotlib.pyplot as plt
Slice=[7,2,2,13]
activities=['sleep','eat','work','play']
colour=['c','m','r','b']

plt.pie(Slice, labels=activities, colors=colour, startangle=90, shadow=True, explode=(0,0.1,0,0), autopct='%1.1f%%')

plt.title("Pie plot")

plt.show()


# #  Multiple Graphs
# **Now we see thw multiple graphs in a single graph**

# In[41]:


import numpy as np 
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()


# In[42]:


import numpy as np 
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(221)
plt.plot(t1, f(t1), 'bo',t2,f(t2))

plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()


# In[ ]:




