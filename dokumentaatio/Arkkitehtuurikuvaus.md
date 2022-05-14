# Arkkitehtuurikuvaus

## Käyttöliittymä

Käyttöliittymä koostuu neljästä päänäkymästä:
- Päävalikko, 0
- Peli, 1
- Statistiikka, 3
- Asetukset, 4

Näkymät on toteutettu niin, että niihin liittyvät tiedot ja pelioliot piirretään näytölle silloin kun muuttuja "game_stage" vastaa niiden arvoa.
"game_stage" on varastoitu "Info"-olioon, ja sen arvot näkyvät yllä olevassa pilkun oikealla puolella. Kaikki pelioliot piirretään "draw"-luokan avulla.

Käyttöliittymä toimii ainoastaan hiirellä, joko klikkaamalla kortteja tai nappeja.

Ohjelman vasemmassa alakulmassa on myös tumma laatikko, joka piirretään jokaisessa pelitilassa. Laatikkoon tulostetaan alun tervetuliasviestien jälkeen
tietoa tietokonepelaajan siirroista pelin aikana. Laatikko on oma olionsa, joka rakennetaan ui/log_window.py avulla, ja saa piirtofunktiossa parametrina
listan. Listasta tulostetaan viimeiset rivit, jotka mahtuvat laatikkoon.

## Sovelluslogiikka

### Info-olio

Info-oliosta löytyy polku kaikkiin ohjelman olioihin, tietoihin ja kuviin.

### Match-olio

Match-oliossa on kaikki varsinaiseen peliin liittyvät tiedot ja pelaajan toiminnot. Sen luonnin yhteydessä luodaan myös olio tietokoneen toiminnoille (Cpl) ja korttiyhdistelmien tarksteluille (Calc). Ohjelmassa voi olla kerrallaan vain yksi Match-olio, joka on varastoitu Info-olioon.

### TIetokone-pelaaja ja Calc-luokka

Cpl-luokka toimii runkona tietokonepelaajan toiminnoille. Kun pelaaja luovuttaa vuoronsa, Match-olio ohjaa suorituksen Cpl:lle, joka päättelee Calc-luokan toimintoja apuna käyttäen, mikä olisi fiksuin siirto tietokonepelaajalle.

Calc-luokassa suoritetaan suurin osa laskutoimituksista. Siellä voidaan laskea painoarvo korteille (card_value), jonka avulla tietokonepelaaja päättää, minkä kortin pelaa pöytään tai mitä kortteja se kaikista eniten haluaa itselleen. Muita funktioita käytetään tarkistamaan, voiko jonkun tietyn yhdistelmän nostaa pöydästä jollain tietyllä kortilla.

### Pakka ja kortit

Deck-luokan avulla luodaan korttipakkaolio. Korttipakkaolio täytetään Card-luokan olioilla, ja se voidaan sekoittaa, täydentää ja kopioida. Pakasta voi nostaa kerrallaan aina yhden päällimmäisen kortin.

Korttioliot luodaan pelin käynnistyksen yhteydessä. Game-luokka kutsuu load_cards-funktioita, joka lataa src/images/cards hakemistosta png-tiedostot, joiden nimi on muodossa <numero>_of_<maa>.png. Nimen perusteella kortille annetaan peliin sopiva käsi- ja pöytäkorttiarvot. load_cards-funktio palauttaa listan korteista ja se annetaan info-oliolle.

### Silmukka

Ohjelman toimii siten, että käynnistyksen jälkeen pyöritään silmukassa niin kauan kunnes ohjelma lopetetaan. Silmukan järjestys on seuraava:
1. Tapahtumien käsittely
2. Näytön taustavärin piirto
3. Peliolioiden piirtäminen
4. Näytön päivitys

Tapahtumien käsittely ohjataan ulkopuoliseen Events-luokkaan.

### Tapahtumien käsittely

Tapahtumat käsitellään Events-luokassa (event_handler.py). Sille lähetetään Loop-luokasta tieto tapahtumasta ja ohjelman info-oliosta. Tapahtumien käsittelijä selvittää info-olion avulla, mikä pelitila on käynnissä, ja sen mukaan tarkistaa onko esimerkiksi päävalikon nappeja painettu. Jos luokka toteaa, että nappia on painettu, muutetaan jonkin muuttujan arvoa tai kutsutaan jotain ulkopuolista funktiota. Esimerkiksi "Settings"-napin painaminen päävalikossa muuttaa "game_stage"n arvon 4:n.

  ## Pelituloksen tallennus
  
  Kun jompikumpi pelaajista voittaa, tallennetaan pisteet tietokantaan db.sqlite nimiseen tiedostoon. 
