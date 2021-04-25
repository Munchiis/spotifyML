#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px

# get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import svm


# In[2]:


df = pd.read_csv("test.csv")
# df.head()
#df.info()


# In[3]:


#extracting columns we will use to base classifications
#dropping unnecessary columns

# UNCOMMENT FOR MEGADATASET
# df.drop(columns=['year', 'release_date', 'id', 'duration_ms', 'artists', 
#                  'name', 'explicit', 'popularity', 'mode', 'key', 'loudness'], inplace=True)

# df.drop(columns=['Unnamed: 0','year','dur','pop'], inplace= True)
# df

# df.drop(columns=['Unnamed: 0'], inplace=True)
# df


# In[4]:


# fig = px.scatter(df, x='bpm', y='nrgy',color='top genre', hover_name='artist',hover_data=['title'])
# fig = px.scatter(df, x='tempo', y='energy',color='genre', hover_name='name', hover_data=['artist'])
# fig.show()


# In[ ]:


k = 5

data = np.array_split(df, k) # split the data into 5 roughly equal groups of samples

print(data)

results = [] # accuracy

# create the support vector machines with the linear, poly, and rbf kernels
clfs = [svm.SVC(kernel="linear"), svm.SVC(kernel="poly"), svm.SVC(kernel="rbf")]

for i in range(k):                                          # run 5 experiments for 5-fold cross-validation
    test_data_set = data[i]                                 # uses one group of data as the test data
    train_data_set = pd.concat(data[:i] + data[i+1:])       # train data takes the rest

    test_labels = np.array(test_data_set.iloc[:, 0])        # use the first column as the label
    print(test_labels)
    test_data = np.array(test_data_set.iloc[:, 3:])         # use the rest for the data

    train_labels = np.array(train_data_set.iloc[:, 0])      # use the first column as the label
    train_data = np.array(train_data_set.iloc[:, 3:])       # use the rest for the data

    experiment_result = []      # the results using each svm for this partitioned data set

    for j in range(len(clfs)):  # use the data set to train each svm
        clfs[j].fit(train_data, train_labels)       # train the svm
        predictions = clfs[j].predict(test_data)    # predict
        accuracy = sum(predictions == test_labels) / len(test_labels)   # get accuracy
        experiment_result.append(accuracy)          # append to the experiment results
        # print((i, j))

    results.append(experiment_result)   # append the row of data to the results

# put the results into a dataframe
results = pd.DataFrame(results)
results.columns = ["Linear", "Poly", "RBF"]

# calculate the average accuracy for each column
avg_accuracy = [sum(results.iloc[:, i]) / len(results) for i in range(3)]
results.loc["Avg"] = avg_accuracy

# display results
print(results)


# In[ ]:





# In[ ]:




