from functions import *

# Instalacja PyPDF2 jeśli nie jest zainstalowane
Install("PyPDF2")

inputDir = "pdf"
# Pobierz listę plików PDF z katalogu
files = tuple(GetPdfFiles(inputDir))

# Wczytaj tekst z plików PDF
texts = ReadPdfFiles(files, inputDir)

outputDir = "output/"
# Dla każdego tekstu znajdź dni tygodnia i utwórz tabele
for i, text in enumerate(texts):
    # Znajdź indeksy wystąpień nazw dni tygodnia
    foundDays = sum(list((map(lambda word: FindAllInStr(text, word), ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]))), [])

    # Wyodrębnij tabele i sformatuj je jako tekst
    tables = list(map(lambda text: FormText(text), list(GetTablesFromText(text, foundDays))))

    # Zapisz wynik do pliku tekstowego w katalogu output/
    WriteToFile(tables, outputDir + files[i].split(".")[0])
