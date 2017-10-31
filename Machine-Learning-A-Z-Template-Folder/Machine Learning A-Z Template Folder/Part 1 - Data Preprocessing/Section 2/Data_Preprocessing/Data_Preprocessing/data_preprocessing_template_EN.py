# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:49:59 2017

@author: Nolaei01
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values

y = dataset.iloc[:,3].values

# missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values ='NaN', strategy ='mean', axis =0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3]  = imputer.transform(X[:,1:3])