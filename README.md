# Kasino (ot-harjoitustyö)

Pythonilla toteutettu [kasino-korttipeli](https://fi.wikipedia.org/wiki/Kasino_(korttipeli)). Kyseessä on yksinpeli, eli peliä pelataan tietokonetta vastaan.

## [Dokumentaatio](https://github.com/Desipeli/ot-harjoitustyo/tree/master/dokumentaatio)

- [vaatimusmäärittely](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Asennusohjeet](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/Asennusohjeet.md)

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
- Korjattu julkaisu viikko 5:lle: [https://github.com/Desipeli/ot-harjoitustyo/releases/tag/viikko5_v2](https://github.com/Desipeli/ot-harjoitustyo/releases/tag/viikko5_v2)

### Viikko 6

- [Viikon 6 julkaisu](https://github.com/Desipeli/ot-harjoitustyo/releases/tag/viikko6)

## Asennusohjeet

[https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/Asennusohjeet.md](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/Asennusohjeet.md)

## Käyttö

### Pelaaminen

1. Siirry komentorivillä pelin päähakemistoon
2. Suorita ``` poetry run invoke start ```
4. Pelaa!

Pelin säännöt löytyvät [täältä](https://github.com/Desipeli/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Pelaaminen windowsilla
1. Siirry powershellillä pelin päähakemistoon
2. suorita ``` poetry run python .\src\index.py ```

Voit myös muokata task.py tiedoston start-funktion muotoon ```ctx.run("python src/index.py", pty=False)```, jonka jälkeen invoke-komento saattaa toimia.
Jos peli-ikkuna venyy liian suureksi, kannattaa tarkistaa näytön asetuksista skaalaus

### Muut

- Testejä voi ajaa komennolla ``` poetry run invoke test ```
- Testikattavuusraportointi ``` poetry run invoke test ``` Löytyy suorituksen jälkeen htmlcov/index.html
- pylint-tarkistus suoritetaan komennolla ``` poetry run invoke lint ```


