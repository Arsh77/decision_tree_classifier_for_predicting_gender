# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 00:44:34 2016

@author: ARSHABH SEMWAL
"""

from sklearn import tree
# [height , weight, shoe size]
X=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[164,65,38],[183,90,49]]
Y=['male','female','female','female','male','male','male','female','male','male','female','male']
clf =tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)

a=input('give us height in cm: ')
b=input('give us weight :')
c=input('give us shoesize: ')
prediction_value=[a,b,c]
prediction=clf.predict([prediction_value])
print(prediction)

