```mermaid
classDiagram
	Pelilauta "1" --> "2-8" Pelaaja
	Pelilauta "1" -- "40" Ruutu
	Pelilauta "1" --> "1" Aloitusruutu
	Pelilauta "1" --> "1" Vankila
	class Pelilauta{
		pelaajat
		ruudut
		aloitusruutu
		vankila
	}
	Pelaaja "1" --> "1" Pelinappula
	Pelaaja "1" --> "*" Raha
	class Pelaaja{
		pelinappula
		rahaa
	}
	class Raha{
	}
	Ruutu "1" --> "1" Ruutu
	Ruutu "1" --> "*" Toiminto
	class Ruutu{
		seuraava_ruutu
	}
	Pelinappula "2-8" --> "1-8" Ruutu
	class Pelinappula{
		ruutu
	}
	Nopat "1" --> "1" Pelaaja
	class Nopat{
		pelaaja
	}
	
	class Toiminto{
		äksön
	}
	Kortti "1" --> "*" Toiminto
	class Kortti{
		toiminto
	}
	
	Aloitusruutu "1" --> "1" Ruutu
	class Aloitusruutu{
		ruutu
	}
	Vankila "1" --> "1" Ruutu
	class Vankila{
		ruutu
	}
	Sattumat_ja_yhteismaat "1" --> "*" Kortti
	Sattumat_ja_yhteismaat "*" --> "*" Ruutu
	class Sattumat_ja_yhteismaat{
		ruutu
		kortit
	}
	Asemat_ja_laitokset "*" --> "*" Ruutu
	class Asemat_ja_laitokset{
		ruutu
	}
	Normaalit_kadut "1" --> "1" Ruutu
	Normaalit_kadut "1" --> "0-4" Talo
	Normaalit_kadut "1" --> "0-1" Hotelli
	Normaalit_kadut "*" --> "1" Pelaaja
	class Normaalit_kadut{
		ruutu
		talot
		hotelli
		pelaaja
	}
	
	class Talo{
	}
	class Hotelli{
	}
