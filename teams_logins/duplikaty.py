# coding: utf-8
import pandas as pd, openpyxl, numpy as np, matplotlib.pyplot as plt
import glob; import os
from unidecode import unidecode
input("Zaznacz cały obszar danych w SharePoint, skopiuj do schowka, a następnie naciśnij Enter.")

df = pd.read_clipboard(dtype = 'str')
df.reset_index(inplace=True, drop=True)
import pandas as pd
from fuzzywuzzy import fuzz

# Załóżmy, że df to Twoja ramka danych
# df = pd.read_csv('your_file.csv')  # Przykład wczytania DataFrame

# Funkcja do znajdowania duplikatów
def find_duplicates(df, cols, threshold=90):
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            # Konwersja wartości do stringów i zastosowanie metody lower()
            values_i = [str(df[col].iloc[i]).lower() for col in cols]
            values_j = [str(df[col].iloc[j]).lower() for col in cols]
            combined_i = ' '.join(values_i)
            combined_j = ' '.join(values_j)
            similarity = fuzz.ratio(combined_i, combined_j)
            if similarity >= threshold:
                print(f"Podobne wpisy w wierszach {i} i {j}: {combined_i} - {combined_j} (Podobieństwo: {similarity}%)")

# Sprawdzanie duplikatów
find_duplicates(df, ['Nazwisko', 'Imię', 'Klasa'])
