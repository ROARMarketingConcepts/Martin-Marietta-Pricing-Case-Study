import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_split_data(path = 'data/creditcard.csv'):
  df = pd.read_csv(path)
  X = df.drop('Class', axis=1)
  y = df['Class']

  # Standardize 'Amount'
  X['Amount'] = StandardScaler().fit_transform(X[['Amount']])

  return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)