#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install matplotlib')


# In[6]:


import matplotlib
print("Installed successfully")


# In[8]:


# Brute Force Detection System
# Author: Your Name
# Description: Detects suspicious IPs based on failed login attempts,
# generates alerts, and visualizes attack patterns

import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("logs.csv")

# Filter failed login attempts
failed = data[data["status"] == "fail"]

# Count failed attempts per IP
counts = failed.groupby("ip").size()

# Detect brute force attacks
threshold = 5
suspicious = counts[counts > threshold]

# Display results
print("\n Failed Login Attempts per IP:\n")
print(counts)

if suspicious.empty:
    print("\n No brute force attack detected")
else:
    print("\n Brute force attack detected from:\n")
    print(suspicious)

# Save alerts to file
suspicious.to_csv("alerts.csv")

# Visualize data
counts.plot(kind='bar')

plt.title("Failed Login Attempts per IP")
plt.xlabel("IP Address")
plt.ylabel("Number of Failed Attempts")

plt.show()


# In[ ]:




