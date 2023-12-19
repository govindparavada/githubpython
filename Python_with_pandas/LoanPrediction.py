import pandas as pd
import numpy as np

df = pd.read_csv('Loans.csv')
df.head()

df.shape

df.info()

from pandas_profiling import ProfileReport

