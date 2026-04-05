#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import plotly
import plotly.offline as py
import plotly.graph_objs as go


trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    name='data1'
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9],
    name="data2"
)
data = [trace0, trace1]

py.offline.plot(data, filename = 'basic-line', auto_open=True)
