# PDF Table Extractor

Aplikacja w Pythonie służąca do ekstrakcji tabel z plików PDF zawierających plany zajęć lub inne dane dzielone wg dni tygodnia.

## Autor
Imię i nazwisko: MAREK NAJBUK  
Nr albumu: [TWÓJ NUMER ALBUMU]

## Wymagania
- Python 3.x
- Biblioteka `PyPDF2` (instalowana automatycznie przez aplikację)

## Struktura katalogów
```
.
├── functions.py
├── main.py
├── pdf/
│   └── pliki_wejsciowe.pdf
├── output/
│   └── wynik.txt
└── README.md
```

## Uruchomienie
1. Umieść pliki PDF w folderze `pdf/`
2. Uruchom aplikację:
```bash
python main.py
```
3. Wyniki zostaną zapisane w folderze `output/` jako pliki `.txt`.

## Opis działania
Program:
- Wyszukuje wzorce dni tygodnia w plikach PDF
- Dzieli tekst na sekcje odpowiadające dniom
- Formatuje je do postaci tabeli w stylu shortcode (np. WordPress)
- Zapisuje dane do pliku tekstowego

## Licencja
Projekt edukacyjny - brak ograniczeń licencyjnych.
