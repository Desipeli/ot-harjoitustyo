```mermaid
classDiagram
	Pelilauta "1" --> "2-8" Pelaaja
	class Pelilauta{
		pelaajat
		ruudut
	}
	class Pelaaja{
		pelinappula
	}
	class Ruutu{
		seuraava_ruutu
	}
	class Pelinappula{
		ruutu
	}
	class Nopat{
		pelaaja
	}
