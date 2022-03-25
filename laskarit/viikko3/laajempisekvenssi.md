```mermaid
sequenceDiagram
	actor main
	participant Kioski
	participant Matkakortti
	participant Lataajalaite
	participant Lukijalaite
	participant HKLLaitehallinto
	main->>HKLLaitehallinto: __init__()
	main->>Lataajalaite: rautatientori
	main->>Lukijalaite: ratikka6
	main->>Lukijalaite: bussi244
	main->>HKLLaitehallinto: lisaa_lataaja(rautatientori)
	Lataajalaite->>HKLLaitehallinto: rautatientori
	main->>HKLLaitehallinto: lisaa_lukija(ratikka6)
	Lukijalaite->>HKLLaitehallinto: ratikka6
	main->>HKLLaitehallinto: lisaa_lukija(bussi244)
	Lukijalaite->>HKLLaitehallinto(bussi244)
	main->>Kioski: lippu_luukku
	main->>Kioski: osta_matkakortti("Kalle"), kallen_kortti
	Kioski->>Matkakortti: __init__("Kalle"), uusi_kortti
	main->>Lataajalaite: lataa_arvoa(kallen_kortti, 3)
	Lataajalaite->>Matkakortti: kasvata_arvoa(3)
	Matkakortti: arvo+=3
	main->>Lukijalaite: osta_lippu(kallen_kortti, 0)
	Kortti->>Lukijalaite: arvo=3
	Lukijalaite->>Matkakortti: vahenna_arvoa(1.5)
	Matkakortti: arvo-=1.5
	main->>Lukijalaite: osta_lippu(kallen_kortti,2)
	Kortti->>Lukijalaite: arvo=1.5, False
	
```
