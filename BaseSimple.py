# -*- coding: utf-8 -*-
"""
Base Model for object location variation in a defined two-dimensional space
Created on Fri Apr 17 21:05:36 2026

@author: rubbensp
"""

# %% packages importeren
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import Geos
import shapely
from shapely.geometry import Polygon, Point

# %% Define room as simple square

room_square1 = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])
print(room_square1)
# %% Define furniture as simple (smaller) square
furniture1 = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
# %%

