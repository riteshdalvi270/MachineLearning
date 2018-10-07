# Predicting Diabetes

import pandas as pd
import matplotlib.pyplot as plt

# Load and review Data

df = pd.read_csv('../data/pima-data.csv')

#print(df.shape)

#print(df.head(5))

#print(df.isnull().values.any())

def plot_corr(df, size=11) :

    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(df.corr())
    plt.xticks(range(len(df.corr().columns)), df.corr().columns)
    plt.yticks(range(len(df.corr().columns)), df.corr().columns)
    #plt.show()

#print(df.corr())

del df['skin']

print(df.head())

plot_corr(df)

diabetes_map = {True: 1, False: 0}

df['diabetes'] = df['diabetes'].map(diabetes_map)

print(df.head())
