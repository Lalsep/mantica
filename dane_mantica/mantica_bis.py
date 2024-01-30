# coding: utf-8
import pandas as pd; import openpyxl; import numpy as np; import matplotlib.pyplot as plt
import glob; import os
files = glob.glob(r'*.xlsx')
df_keys = pd.read_excel(files[2], sheet_name=None).keys()
db = pd.read_csv('../import_uczniow.csv', encoding = 'windows-1250', sep = ';', dtype = str)
import unidecode
db.columns = [unidecode(x) for x in db.columns]
# %load mantica.py
def przetworz_pesel(pesel):
    # Sprawdzanie, czy wpis jest prawdopodobnym PESEL (11 cyfr)
    if pesel.isdigit() and len(pesel) == 11:
        return pesel
    elif pesel.isdigit() and len(pesel) == 10:
        return '0' + pesel
    else:
        return None  # lub można zwrócić np. 'Nieprawidłowy'

# Zastosowanie funkcji do kolumny PESEL
df['pesel'] = df['pesel'].astype(str).apply(przetworz_pesel)

# Usunięcie wierszy z nieprawidłowymi danymi PESEL
df = df[df['pesel'].notnull()]

# Obliczenie daty urodzenia i dodanie jako nowa kolumna
df['data urodzenia'] = df['pesel'].apply(oblicz_date_urodzenia)
def przetworz_pesel(pesel):
    # Sprawdzanie, czy wpis jest prawdopodobnym PESEL (11 cyfr)
    if pesel.isdigit() and len(pesel) == 11:
        return pesel
    elif pesel.isdigit() and len(pesel) == 10:
        return '0' + pesel
    else:
        return None  # lub można zwrócić np. 'Nieprawidłowy'

# Zastosowanie funkcji do kolumny PESEL
df['pesel'] = df['pesel'].astype(str).apply(przetworz_pesel)

# Usunięcie wierszy z nieprawidłowymi danymi PESEL
df = df[df['pesel'].notnull()]

# Obliczenie daty urodzenia i dodanie jako nowa kolumna
df['data urodzenia'] = df['pesel'].apply(oblicz_date_urodzenia)
def przypisz_plec(db):
    # Funkcja pomocnicza do określenia płci na podstawie nazwiska i imienia
    def okresl_plec(row):
        nazwisko, imie = row['nazwisko'], row['imię']
        
        # Sprawdzenie, czy nazwisko lub imię kończy się na 'a'
        if pd.isnull(nazwisko) and pd.isnull(imie):
            return 'Nieznana'  # lub inna wartość dla pustych/nieznanych
        if (nazwisko and nazwisko.endswith('a')) or (imie and imie.endswith('a')):
            return 'k'
        return 'm'

    # Stworzenie nowej kolumny 'Płęć' z wartościami przypisanymi na podstawie nazwiska i imienia
    db['Płęć'] = db.apply(
    okresl_plec, axis=1)

    return db
    

def przetworz_dane(df):
    # Funkcja do obliczenia daty urodzenia z numeru PESEL
    def oblicz_date_urodzenia(pesel):
        if pd.isnull(pesel) or not str(pesel).isdigit() or len(str(pesel)) != 11:
            return 'Nieznana'
        rok = int(pesel[:2])
        miesiac = int(pesel[2:4])
        dzien = int(pesel[4:6])
        if miesiac > 80:
            rok += 1800
            miesiac -= 80
        elif miesiac > 60:
            rok += 2200
            miesiac -= 60
        elif miesiac > 40:
            rok += 2100
            miesiac -= 40
        elif miesiac > 20:
            rok += 2000
            miesiac -= 20
        else:
            rok += 1900
        return f"{rok}-{miesiac:02d}-{dzien:02d}"

    # Funkcja do określenia płci na podstawie nazwiska i imienia
    def okresl_plec(row):
        nazwisko, imie = row['nazwisko'], row['imie']
        if (nazwisko and not nazwisko.endswith('a')) or (imie and not imie.endswith('a')):
            return 'm'
        return 'k'

    # Obliczenie daty urodzenia i dodanie jako nowa kolumna
    df['data urodzenia'] = df['pesel'].apply(oblicz_date_urodzenia)

    # Stworzenie nowej kolumny 'Płęć' z wartościami przypisanymi na podstawie nazwiska i imienia
    df['plec'] = df.apply(okresl_plec, axis=1)

    return df

# Przykładowe użycie
df = przetworz_dane(df)
print(df)

def przetworz_dane(df):
    # Funkcja do obliczenia daty urodzenia z numeru PESEL
    def oblicz_date_urodzenia(pesel):
        if pd.isnull(pesel) or not str(pesel).isdigit() or len(str(pesel)) != 11:
            return 'Nieznana'
        rok = int(pesel[:2])
        miesiac = int(pesel[2:4])
        dzien = int(pesel[4:6])
        if miesiac > 80:
            rok += 1800
            miesiac -= 80
        elif miesiac > 60:
            rok += 2200
            miesiac -= 60
        elif miesiac > 40:
            rok += 2100
            miesiac -= 40
        elif miesiac > 20:
            rok += 2000
            miesiac -= 20
        else:
            rok += 1900
        return f"{rok}-{miesiac:02d}-{dzien:02d}"

    # Funkcja do określenia płci na podstawie nazwiska i imienia
    def okresl_plec(row):
        nazwisko, imie = row['nazwisko'], row['imiona']
        if (nazwisko and not nazwisko.endswith('a')) or (imie and not imie.endswith('a')):
            return 'm'
        return 'k'

    # Obliczenie daty urodzenia i dodanie jako nowa kolumna
    df['data urodzenia'] = df['pesel'].apply(oblicz_date_urodzenia)

    # Stworzenie nowej kolumny 'Płęć' z wartościami przypisanymi na podstawie nazwiska i imienia
    df['plec'] = df.apply(okresl_plec, axis=1)

    return df

# Przykładowe użycie
df = przetworz_dane(df)
print(df)

def dopisz_zera_do_pesel(df):
    def przetworz_pesel(pesel):
        # Sprawdzanie, czy PESEL składa się tylko z cyfr
        if str(pesel).isdigit():
            # Dopisywanie zer na początku, jeśli długość PESEL jest mniejsza niż 11
            return str(pesel).zfill(11)
        else:
            # Zostawienie pustego miejsca, jeśli PESEL zawiera litery
            return ''

    df['pesel'] = df['pesel'].apply(przetworz_pesel)
    return df

# Przykładowe użycie
df = dopisz_zera_do_pesel(df)
print(df)
