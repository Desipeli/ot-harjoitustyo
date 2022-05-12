# Käyttöohje

## Käynnistäminen

### Linux

1. Siirry komentorivillä pelin päähakemistoon
2. Suorita ``` poetry run invoke start ```

### Windows
1. Siirry powershellillä pelin päähakemistoon
2. suorita ``` poetry run invoke startwindows ```

Jos peli-ikkuna venyy liian suureksi, kannattaa tarkistaa näytön asetuksista skaalaus

### Testit

- Testejä voi ajaa komennolla ``` poetry run invoke test ```
- Testikattavuusraportointi ``` poetry run invoke coverage-report ``` Löytyy suorituksen jälkeen htmlcov/index.html
- pylint-tarkistus suoritetaan komennolla ``` poetry run invoke lint ```

## Pelaaminen ja navigointi

- Peliä pelataan ainoastaan hiirtä käyttäen.
- Päävalikosta voi aloittaa uuden pelin painamalla ``` Play ``` nappia.
- Pelaajan käsikortit näkyvät ruudun alareunassa keskellä. Valittu käsikortti on hieman korkeammalla kuin muut. Kortti valitaan klikkaamalla sitä.
- Pöytäkortit näkyvä ruudun keskiosassa. Valitut pöytäkortit ovat hieman korkeammalla muihin verrattuna. Pöytäkortteja valitaan tai valinta poistetaan klikkaamalla korttia.
- Pelaaja hyväksyy kaikki toimenpiteet omien korttien oikealla puolella olevalla napilla.
    - Jos yhtäkään pöytäkorttia ei ole valittu, pelataan valittu käsikortti pöytään ja vuoro siirtyy tietokoneelle.
    - Jos pöytäkortteja on valittu, ja ne voidaan nostaa valitulla käsikortilla, saa pelaaja ne omaan pinoonsa ja vuoro siirtyy tietokoneelle.
    - Jos pöytäkortteja ei voi nostaa, tulee pöytäkorttien alle virheilmoitus eikä vuoro vaihdu.
    - Tietokoneen aloittamalla kierroksella pelaajan on painettava nappia ennen kuin kierros alkaa.
- Tietokoneen kortit näkyvät ruudun yläreunassa keskellä. Ne ovat oletuksena käännettynä väärin päin, mutta asetuksista voi säätää ne näkyviin.

- Jos pelin aikana palaa päävalikkoon, voi peliä jatkaa painamalla valikosta ``` Continue ``` nappia

## Statistiikka ja asetukset

- Päävalikosta pääsee muuttamaan pelin asetuksia painamalla ``` Settings ``` nappia. Toistaiseksi vain tietokoneen korttien piilottaminen/näyttäminen löytyy täältä.
-  Päävalikosta pääsee myös katsomaan pelitilastoa. ``` Stats ``` nappi ohja näkymään, josta selviää kuinka monta peliä pelaaja on voittanut tietokonetta vastaan.

## Loki-ikkuna

- Ohjelman vasemmassa alakulmassa on musta laatikko, johon tulostuu tekstinä tietokoneen tekemät siirrot. Tämä helpottaa hahmottamaan pelin tapahtumia.

## Säännöt

### Pelin kulku

Alussa kortit jaetaan seuraavalla tavalla:
1. pelaajalle 2
2. jakajalle 2
3. pöytään 2
4. toistetaan kerran
Jolloin sekä pelaajilla että pöydässä on 4 korttia.

Pelaajat voivat nostaa vuorollaa yhdellä käsikortilla kaikki ne yhdistelmät pöydästä, jotka muodostavat käsikortin arvon.
Esimerkiksi ruutu kuninkaalla voisi nostaa yhdellä nostolla pata kunkun, risti seiskan ja hertta kutosen. Kunkku (13) = Kunkku (13) ja 7 + 6 = 13. 
Jos pelaaja ei voi nostaa pöydästä mitään, pelataan jokin käsikorteista pöytään.
Pöydästä ei ole pakko nostaa kortteja, mutta joka vuoro on pelattava yksi kortti.

Kun molempien käsikortit on pelattu, jaetaan pakasta uudet kortit samaan tyyliin kuin alussa, mutta ei jaeta pöytään.
Kierros päättyy kun pakka on tyhjä. Viimeiseksi nostanut pelaaja saa pöytään jääneet kortit.

Peliä pelataan 16 pisteeseen asti. Kasino voi päättyä aina kun käsikortit on pelattu, jos ainakin toisella 16 pistettä.

### Erikoiskortit

- Ässä on pöydässä 1, kädessä 14
- Patakakkonen on pöydässä 2, kädessä 15
- Ruutukymppi on pöydässä 10, kädessä 16

### Pisteet

- Eniten kortteja kerännyt pelaaja  1 piste
- Eniten pataa kerännyt pelaaja     2 pistettä
- Ässät                             1 piste/kortti
- Ruutukymppi                       2 pistettä
- Patakakkonen                      1 piste

Pelissä voi myös kerätä mökkejä. Jos pelaaja tyhentää pöydän kun pakassa on vielä kortteja, eikä kummallakaan ole vielä kymmentä pistettä, hän saa yhden pistee arvoisen "mökin".
Jos toisella pelaajalla on yksi tai useampi mökki, poistetaan niistä yksi eikä pöydän tyhjentänyt saa mökkiä.
