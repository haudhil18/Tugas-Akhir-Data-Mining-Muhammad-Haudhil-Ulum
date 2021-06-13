# -*- coding: utf-8 -*-
"""Prediksi Kemungkinan Seseorang Terkena Gagal Jantung.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O9odFeTzfABTKxywtVSIJuIR7F_fePGJ
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("heart_failure_dataset.csv")
dataset

sns.countplot(x='DEATH_EVENT', data=dataset)

sns.countplot(x='DEATH_EVENT',data=dataset,hue='high_blood_pressure')

dataset.drop(['anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','serum_creatinine','serum_sodium','sex','smoking', 'time'], 
             axis=1,inplace=True)
dataset

from sklearn.model_selection import train_test_split
x=dataset.drop('DEATH_EVENT',axis=1)
y=dataset['DEATH_EVENT']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

print(x_train)

print(x_test)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)
dataset1=pd.DataFrame({'Data Aktual Terkena Gagal Jantung' :y_test,'Data Prediksi Terkena Gagal Jantung':y_pred})
dataset1

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min()-1, stop = x_set[:, 0].max() + 1, step=0.01),
                     np.arange(start = x_set[:, 1].min()-1, stop = x_set[:, 0].max() + 1, step=0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75, cmap= ListedColormap(('blue', 'yellow')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate (np.unique(y_set)):
  plt.scatter(x_set[y_set == j, 0], x_set[y_set==j, 1],
              c = ListedColormap(('blue', 'yellow'))(j), label = j)
plt.title('Klasifikasi Data dengan Native Bayes (Data Training)')
plt.xlabel('Age (Umur)')
plt.ylabel('Platelets (Trombosit)')
plt.legend()
plt.show

from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
            alpha = 0.75, cmap = ListedColormap(('blue','yellow')))
plt.xlim(x1.min(),x1.max())
plt.xlim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
  plt.scatter(x_set[y_set == j, 0],x_set[y_set == j, 1],
              c = ListedColormap(('blue','yellow'))(i),label = j)
plt.title('Klasifikasi Data dengan Naive Bayes(Data Testing)')
plt.xlabel('Age (Umur)')
plt.ylabel('Platelets (Trombosit)')
plt.legend()
plt.show()

print(accuracy_score(y_test, y_pred)*100)