# Vaatimusmäärittely

# Pelin idea

Harjoitustyö on tietokonetta vastaan pelattava korttipeli kasino. 

## Perusversion toiminnallisuus

- Peliä pelataan pääasiassa hiirellä 
- Graafinen käyttöliittymä koostuu ainakin päävalikosta, pelipöydästä sekä highscore-näkymästä

## Tämän hetken toiminnallisuudet

- Pelaaja voi ottaa kortteja pöydästä ainoastaan sääntöjen sallimissa rajoissa
- Tietokone osaa arvioida ja nostaa järkevän korttiyhdistelmän pöydästä
- Pelaaja aloittaa aina ensimmäisen erän, tietokone seuraavan. Aloittaja vaihtuu joka vuoro
- Peli päättyy kun toisella on vähintään 16 pistettä, käsikortit on pelattu eikä ole tasapelitilannetta.
- Peli toimii alla olevien sääntöjä noudattaen
- Peliä voi pelata ainoastaan hiirellä

## Puuttuvat toiminnallisuudet
 
 - Tietokone voisi arvioida tarkemmin pöydälle pelattavaa korttia
 - Voittotilastoja ei vielä tallenneta mihinkään
 - Asetukset-näkymä, jossa voi valita esimerkiksi minkä näköistä korttipakkaa käytetään
 - UI:n hiomista, ehkä yksinkertainen animaation korttien siirtymisiin

## Jos aikaa riittää

- Toteutetaan myös kesken jääneen pelin tallentaminen ja jatkaminen myöhemmin.
- Mahdollisuus muuttaa sääntöjä. Pelistä on useita eri versioita, joten jokainen voi tuunata mieleisekseen.

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

Pelissä voi myös kerätä mökkejä. Jos pelaaja tyhentää pöydän kun pakassa on vielä kortteja, eikä kummallakaan ole vielä kymmentä pistettä, hän saa yhden pistee arvoisen "mökin".
Jos toisella pelaajalla on yksi tai useampi mökki, poistetaan niistä yksi eikä pöydän tyhjentänyt saa mökkiä.
