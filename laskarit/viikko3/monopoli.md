```mermaid
classDiagram
	Pelilauta "1" --> "2-8" Pelaaja
	Pelilauta "1" -- "40" Ruutu
	class Pelilauta{
		pelaajat
		ruudut
	}
	Pelaaja "1" --> "1" Pelinappula
	class Pelaaja{
		pelinappula
	}
	Ruutu "1" --> "1" Ruutu
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
