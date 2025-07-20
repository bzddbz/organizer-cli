@echo off
echo.
echo ============================================
echo          FILE ORGANIZER CLI
echo ============================================
echo.
echo Valassz rendszerezesi modot:
echo.
echo 1. Kiterjesztes szerint
echo 2. Fajltipus szerint (kepek, dokumentumok, stb.)
echo 3. Datum szerint (ev)
echo 4. Datum szerint (honap)
echo 5. Datum szerint (nap)
echo 6. Meret szerint
echo 7. Elonezet - kiterjesztes szerint
echo 8. Elonezet - fajltipus szerint
echo 9. Kilep
echo.
set /p choice="Valaszd ki a szamot (1-9): "

if "%choice%"=="1" (
    python file_organizer.py --method extension
) else if "%choice%"=="2" (
    python file_organizer.py --method type
) else if "%choice%"=="3" (
    python file_organizer.py --method date --date-format year
) else if "%choice%"=="4" (
    python file_organizer.py --method date --date-format month
) else if "%choice%"=="5" (
    python file_organizer.py --method date --date-format day
) else if "%choice%"=="6" (
    python file_organizer.py --method size
) else if "%choice%"=="7" (
    python file_organizer.py --preview --method extension
) else if "%choice%"=="8" (
    python file_organizer.py --preview --method type
) else if "%choice%"=="9" (
    exit
) else (
    echo Ervenytelen valasztas!
    pause
    goto :eof
)

echo.
pause
