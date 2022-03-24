# Vaatimusmäärittely

# Pelin idea

Harjoitustyö on tietokonetta vastaan pelattava korttipeli kasino. 

## Säännöt

### Pelin kulku

Alussa kortit jaetaan seuraavalla tavalla:
1. pelaajalle 2
2. jakajalle 2
3. pöytään 2
4. toistetaan kerran
Jolloin sekä pelaajilla että pöydässä on 4 korttia.

Pelaajat voivat nostaa vuorollaa yhdellä käsikortilla ne kortit pöydästä, joiden summa muodostaa käsikortin arvon.
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

Pelissä voi myös kerätä mökkejä. Jos pelaaja tyhentää pöydän kun pakassa on vielä kortteja, hän saa yhden pistee arvoisen "mökin".
Jos toisella pelaajalla on yksi tai useampi mökki, poistetaan niistä yksi eikä pöydän tyhjentänyt saa mökkiä.
