# coding: utf-8
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
        nazwisko, imie = row['Nazwisko'], row['Imię']
        
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
    
