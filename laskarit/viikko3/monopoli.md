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
	
	Aloitusruutu "1" --> "1" Ruutu
	class Aloitusruutu{
		ruutu
	}
	Vankila "1" --> "1" Ruutu
	class Vankila{
		ruutu
	}
	Sattumat_ja_yhteismaat "*" --> "*" Ruutu
	class Sattumat_ja_yhteismaat{
		ruutu
	}
	Asemat_ja_laitokset "*" --> "*" Ruutu
	class Asemat_ja_laitokset{
		ruutu
	}
	Normaalit_kadut "*" --> "*" Ruutu
	class Normaalit_kadut{
		ruutu
	}
