# coding: utf-8
# %load plik_eksportu.py
input("Zaznacz obszar z nowymi uczniami w SharePoint, skopiuj do schowka, a następnie naciśnij Enter.")

db = pd.read_clipboard(header=None, names =df.columns, dtype = 'str')
dc = pd.read_csv('Import_User_Template.csv', dtype = 'str')
from unidecode import unidecode
db.rename(columns = {'Nazwisko':'Imię', 'Imię':'Nazwisko'}, inplace = True)
db['Imię'] = db['Imię'].str.split(' ').str[0]
# Funkcja do transformacji imienia i nazwiska
def create_username(row):
    imie = unidecode(row['Imię'].strip().lower())
    nazwisko = unidecode(row['Nazwisko'].strip().lower())
    return f"{imie}.{nazwisko}@otwartaszkola.pl"

# Stosowanie funkcji do każdego wiersza DataFrame
db['Nazwa użytkownika'] = db.apply(create_username, axis=1)
mapowanie = {'Klasa':'Stanowisko','email':'Alternatywny adres e-mail'}
db.rename(columns = mapowanie, inplace = True)
for e in db.columns:
    if e in dc.columns:
        dc[e] = db[e]
        
dc
