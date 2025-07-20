# File Organizer CLI

Egy Python-alapú CLI alkalmazás, amely automatikusan rendszerezi a fájlokat egy mappában különböző kritériumok szerint.

## Funkcionalitás

### Rendszerezési módok

1. **Kiterjesztés szerint** (`--method extension`)
   - Fájlokat kiterjesztés alapján csoportosítja
   - Példa: `jpg_files/`, `pdf_files/`, `txt_files/`

2. **Fájltípus szerint** (`--method type`)
   - Fájlokat kategóriák szerint csoportosítja:
     - `images/` - képek (jpg, png, gif, stb.)
     - `documents/` - dokumentumok (pdf, docx, txt, stb.)
     - `videos/` - videók (mp4, avi, mkv, stb.)
     - `audio/` - hangfájlok (mp3, wav, flac, stb.)
     - `archives/` - tömörített fájlok (zip, rar, 7z, stb.)
     - `code/` - programkódok (py, js, html, stb.)
     - `executables/` - futtatható fájlok (exe, msi, stb.)
     - `data/` - adatfájlok (json, xml, csv, stb.)
     - `others/` - egyéb fájlok

3. **Dátum szerint** (`--method date`)
   - `--date-format year` - évek szerint (2024/, 2025/)
   - `--date-format month` - hónapok szerint (2024-01/, 2024-02/)
   - `--date-format day` - napok szerint (2024-01-15/, 2024-01-16/)

4. **Méret szerint** (`--method size`)
   - `small_files/` - < 1KB
   - `medium_files/` - 1KB - 1MB
   - `large_files/` - 1MB - 100MB
   - `huge_files/` - > 100MB

### Opciók

- `--preview` - Csak előnézet, nem mozgatja a fájlokat
- `--target-dir` - Cél könyvtár neve (alapértelmezett: `organized_files`)
- `--include-hidden` - Rejtett fájlok is bekerülnek a rendszerezésbe

## Használat

### Közvetlen parancssor

```bash
# Kiterjesztés szerint rendszerezés
python file_organizer.py --method extension

# Fájltípus szerint rendszerezés
python file_organizer.py --method type

# Dátum szerint rendszerezés (hónapok szerint)
python file_organizer.py --method date --date-format month

# Méret szerint rendszerezés
python file_organizer.py --method size

# Előnézet kiterjesztés szerint
python file_organizer.py --preview --method extension

# Egyéni cél könyvtár
python file_organizer.py --method type --target-dir my_organized_files

# Rejtett fájlok is
python file_organizer.py --method extension --include-hidden
```

### Interaktív batch fájl (Windows)

```batch

# File Organizer CLI

Egyszerű Python script, amely különböző szempontok szerint rendszerezi a fájlokat egy mappában.

## Használat

```bash
python file_organizer.py --method <módszer> [--source-dir <elérési út>]
```

### Elérhető módszerek:
- `extension` - kiterjesztés szerint
- `type` - fájltípus szerint
- `date` - módosítás dátuma szerint
- `size` - fájlméret szerint

### További opciók:
- `--source-dir` - forrás könyvtár elérési útja (alapértelmezett: aktuális mappa)
- `--date-format` - dátum formátuma (`year`, `month`, `day`)
- `--preview` - csak előnézet, nem mozgatja a fájlokat
- `--target-dir` - cél könyvtár neve (alapértelmezett: `organized_files`)
- `--include-hidden` - rejtett fájlok is

### Példák

```bash
# Kiterjesztés szerint rendszerezés az aktuális mappában
python file_organizer.py --method extension

# Fájltípus szerint rendszerezés egy megadott mappában
python file_organizer.py --method type --source-dir "C:\Users\bence\Documents"

# Hónap szerint rendszerezés
python file_organizer.py --method date --date-format month

# Méret szerint rendszerezés
python file_organizer.py --method size

# Előnézet kiterjesztés szerint
python file_organizer.py --preview --method extension
```
--------------------------------------------------

📁 images/ (8 fájl)
  • photo1.jpg
  • screenshot.png
  • avatar.gif
  • banner.svg
  • icon.ico

📁 documents/ (12 fájl)
  • report.pdf
  • notes.txt
  • presentation.pptx
  • spreadsheet.xlsx
  • document.docx

📁 archives/ (3 fájl)
  • backup.zip
  • project.rar
  • data.7z

📁 others/ (2 fájl)
  • config.cfg
  • readme.log
```

## Hibaelhárítás

### Gyakori hibák

1. **"Permission denied"** - Fájl használatban van, zárd be az alkalmazást
2. **"File not found"** - Fájl már át lett mozgatva vagy törölve
3. **"Python not found"** - Python nincs telepítve vagy PATH-ban

### Tippek

- Mindig használd az `--preview` opciót először
- Készíts biztonsági mentést fontos fájlokról
- Nagyobb mappákban tesztelj kisebb almappákon előbb

## Licenc

MIT License - Szabadon használható és módosítható.
