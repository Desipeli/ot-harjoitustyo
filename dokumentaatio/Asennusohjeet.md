# Asennusohjeet

Pelin toimivuus on testattu python versioilla: 3.8.10, 3.10.4, 3.9.7

## Pelin asennus

- Lataa [uusin julkaisu](https://github.com/Desipeli/ot-harjoitustyo/releases)
- Pura tiedostot haluamaasi hakemistoon
- siirry komentorivillä pelin päähakemistoon ja suorita ``` poetry install ```
- Luo tietokanta pelille:
  - Linux: Pysy edelleen pelin päähakemistossa ja suorita ``` poetry run invoke build ```
  - Windows: Pysy edelleen pelin päähakemistossa ja suorita ``` poetry run invoke buildwindows ```

## Jos koneellasi ei ole pythonia ja/tai poetrya

### Pythonin asennus Windowsille

1. Lataa asennuspaketti [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Varmista asennuksen aikana että ``` pip ``` on valittu
3. Varmista myös että python lisätään ympäristömuuttujiin
4. Jos powershell tai cmd oli asennuksen aikana auki, kannattaa se käynnistää uudelleen

Tarkempia ohjeita löytyy esimerkiksi. [https://phoenixnap.com/kb/how-to-install-python-3-windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

### Poetryn asennus Windowsille

#### Tapa 1

1. Suorita powershellissä ``` pip install poetry```

#### Tapa 2

1. Suorita ``` (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python - ``` Powershellissä (cmd:ssä ei välttämättä toimi)
2. Lisää ilmoitettu polku ympäristömuuttujaan

### poetryn asennus Linuxille

1. Suorita terminaalissa ``` pip install poetry```


Asenna peli!
