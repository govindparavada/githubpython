import numpy as np
import pandas as pd

# data_with_headers.csv
fileName = input("enter file name:")
dataFile = pd.read_csv(fileName)

print(dataFile[0:3])

