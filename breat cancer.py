# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TlFocy8fP6tXgECYt4IGN74_5Dn6XlQ0
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data=pd.read_csv('/content/breast-cancer.csv')

"""# **Data**"""

data.head()

data.info()

data.isna().sum()

data.describe()

"""**outlaier**"""

def remove_outliers_all_columns(data):
    for column in data.select_dtypes(include=['number']).columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1


        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR


        df = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data

df_filtered_all = remove_outliers_all_columns(data)
print("Filtered DataFrame for all columns:")
print(df_filtered_all)

encoder=LabelEncoder()
for column in data.select_dtypes(include=['object']).columns:
    data[column] = encoder.fit_transform(data[column])

plt.figure(figsize=(10,8))
sns.heatmap(data,annot=True,cmap='coolwarm')
plt.show()

X=data.drop(['diagnosis'],axis=1)
y=data['diagnosis']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=24,shuffle=True)

clf = DecisionTreeClassifier(criterion='gini', max_depth=3)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"دقة النموذج: {accuracy:.2f}")

plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=X.columns, class_names=list(map(str, clf.classes_)), filled=True)
plt.title("Decision Tree Visualization")
plt.show()