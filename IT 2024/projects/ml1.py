import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r'projects\train.csv')
print(df.head())
df.info()
df.describe().T
df['ethnicity'].value_counts()
df['relation'].value_counts()
df = df.replace({'yes':1, 'no':0, '?':'Others', 'others':'Others'})
plt.pie(df['Class/ASD'].value_counts().values, autopct='%1.1f%%')
plt.show()
ints = []
objects = []
floats = []

