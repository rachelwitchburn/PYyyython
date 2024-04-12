import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv(r'C:\Users\raque\OneDrive\Área de Trabalho\PYthon\arq csv spotify\spotify (1).csv')
print(df)
df.sort_values('song_popularity', ascending=False, inplace=True)
print(df.head(15))
df.head()
df.info()
df.describe()

duplicados = df[df.duplicated(keep='first')]
print(duplicados)
df.drop_duplicates(keep='first', inplace=True)

def remove_units (DataFrame, columns, what):
    for col in columns:
        DataFrame[col] = DataFrame[col].str.strip(what)

remove_units(df, ['acousticness', 'danceability'], 'mol/L')
remove_units(df, ['song_duration_ms', 'acousticness'], 'kg')

print(type(np.nan))
df = df.replace(['nao_sei'], np.nan)
df['key'] = df['key'].replace([0.177], np.nan)
df['audio_mode'] = df['audio_mode'].replace(['0.105'], np.nan)
df['speechiness'] = df['speechiness'].replace(['0.nao_sei'], np.nan)
df['time_signature'] = df['time_signature'].replace(['0.7', '2800000000'], np.nan)

