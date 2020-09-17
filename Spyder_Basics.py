#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:54:15 2020

@author: aireesrondain
"""

import pandas as pd

## this is a comment
# comments do not execute

df = pd.read_csv('DataSeerGrabPrizeData.csv')

df.describe()

df.dropna()

df.describe()

df.to_csv('grab_on_spyder.csv', index=False)