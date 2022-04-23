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

## Asennusohjeet

1. Pura tiedosto haluamaasi hakemistoon
2. Suorita ``` poetry install ```

### python 3 asennus windowsille

1. lataa asennuspaketti [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Asenna ja käynnistä powershell uudestaan jos se oli auki

### poetryn asennus windowsille

1. Suorita ``` (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python - ``` Powershellissä (cmd:ssä ei välttämättä toimi)
2. Lisää ilmoitettu polku ympäristömuuttujaan

## Käyttö

### Pelaaminen

1. Siirry komentorivillä pelin päähakemistoon
2. Suorita ``` poetry run invoke start ```
3. Pelaa!

### Pelaaminen windowsilla
1. suorita ``` poetry shell```
2. suorita ``` python .\src\index.py ```
Toistaiseksi invoke-komennot eivät toimi windowsilla. Peli saattaa venyä koko näytölle...

### Muut

- Testejä voi ajaa komennolla ``` poetry run invoke test ```
- Testikattavuusraportointi ``` poetry run invoke test ``` Löytyy suorituksen jälkeen htmlcov/index.html
- pylint-tarkistus suoritetaan komennolla ``` poetry run invoke lint ```


