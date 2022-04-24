# Kasino (ot-harjoitustyö)

Pythonilla toteutettu [kasino-korttipeli](https://fi.wikipedia.org/wiki/Kasino_(korttipeli)). Kyseessä on yksinpeli, eli peliä pelataan tietokonetta vastaan.

## [Dokumentaatio](https://github.com/Desipeli/ot-harjoitustyo/tree/master/dokumentaatio)

- [vaatimusmäärittely](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Laskarit

### Viikko 1
- [gitlog.txt](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

- [komentorivi.txt](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)

### [viikko 2](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko2/)

- [testikattavuus](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko2/testikattavuus)

### Viikko 3

- [monopolikaavio](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko3/monopoli.md)
- [sekvenssikaavio](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko3/sekvenssi.md)
- [laajempi sekvenssikaavio](https://github.com/Desipeli/ot-harjoitustyo/blob/master/laskarit/viikko3/laajempisekvenssi.md)

### Viikko 5

- Ensimmäinen julkaisu [https://github.com/Desipeli/ot-harjoitustyo/releases/tag/viikko5](https://github.com/Desipeli/ot-harjoitustyo/releases/tag/viikko5)

## Asennusohjeet

Pelin toimivuus on testattu python versioilla: 3.8.10, 3.10.4, 3.9.7

1. Pura tiedosto haluamaasi hakemistoon
2. Suorita komentorivillä pelin päähakemistossa ``` poetry install ```

### Jos python ja/tai poetry puuttuu
### python 3 asennus windowsille

1. lataa asennuspaketti [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Asenna oletusasetuksilla. Varmista että pip on valittu
3. Jos powershell tai komentorivi oli asennuksen aikana auki, kannattaa se sulkea ja avata uudestaan

### poetryn asennus windowsille

#### tapa 1
1. suorita ``` pip install poetry ```

#### tapa 2

3. Suorita ``` (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python - ``` Powershellissä (cmd:ssä ei välttämättä toimi)
4. Lisää ilmoitettu polku ympäristömuuttujaan

Tarkempia ohjeita löytyy esimerkiksi. [https://phoenixnap.com/kb/how-to-install-python-3-windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

## Käyttö

### Pelaaminen

1. Siirry komentorivillä pelin päähakemistoon
2. Suorita ``` poetry run invoke start ```
3. Pelaa!

### Pelaaminen windowsilla
1. Siirry powershellillä pelin päähakemistoon
2. suorita ``` poetry shell```
3. suorita ``` python .\src\index.py ```

Voit myös muokata task.py tiedoston start-funktion muotoon ```ctx.run("python src/index.py", pty=False)```, jonka jälkeen invoke-komento saattaa toimia.
Jos peli-ikkuna venyy liian suureksi, kannattaa tarkistaa näytön asetuksista skaalaus

### Muut

- Testejä voi ajaa komennolla ``` poetry run invoke test ```
- Testikattavuusraportointi ``` poetry run invoke test ``` Löytyy suorituksen jälkeen htmlcov/index.html
- pylint-tarkistus suoritetaan komennolla ``` poetry run invoke lint ```


