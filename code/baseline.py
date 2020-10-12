import numpy as np
import pandas as pd
train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/testA.csv')
sample_submit = pd.read_csv('../data/sample_submit.csv',nrows= 10)
print(666)
print(train.info())
print(test.info())
print(sample_submit)