import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kp = Kassapaate()
        self.mk = Maksukortti(1000)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.kp.kassassa_rahaa, 100000)
    
    def test_myytyjen_lounaiden_maara_alussa_0(self):
        self.assertEqual(self.kp.edulliset+self.kp.maukkaat, 0)
    # Edulliset käteinen
    def test_kateisosto_edullisesti_tasaraha(self):
        vaihtoraha = self.kp.syo_edullisesti_kateisella(240)
        self.assertEqual((self.kp.edulliset, self.kp.kassassa_rahaa, vaihtoraha), (1, 100240, 0))
    
    def test_kateisosto_edullisesti_liian_vahan_rahaa(self):
        vaihtoraha = self.kp.syo_edullisesti_kateisella(200)
        self.assertEqual((self.kp.edulliset, self.kp.kassassa_rahaa, vaihtoraha), (0, 100000, 200))
    
    def test_kateisosto_edullisesti_liikaa_rahaa(self):
        vaihtoraha = self.kp.syo_edullisesti_kateisella(400)
        self.assertEqual((self.kp.edulliset, self.kp.kassassa_rahaa, vaihtoraha), (1, 100240, 160))
    # Maukkaat käteinen
    def test_kateisosto_maukkaat_tasaraha(self):
        vaihtoraha = self.kp.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kp.maukkaat, self.kp.kassassa_rahaa, vaihtoraha), (1, 100400, 0))
    
    def test_kateisosto_maukkaat_liian_vahan_rahaa(self):
        vaihtoraha = self.kp.syo_maukkaasti_kateisella(200)
        self.assertEqual((self.kp.maukkaat, self.kp.kassassa_rahaa, vaihtoraha), (0, 100000, 200))
    
    def test_kateisosto_maukkaat_liikaa_rahaa(self):
        vaihtoraha = self.kp.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kp.maukkaat, self.kp.kassassa_rahaa, vaihtoraha), (1, 100400, 100))
 
    # korttitestit

    def test_kortilla_tarpeeksi_rahaa_edullinen(self):
        onnistuiko = self.kp.syo_edullisesti_kortilla(self.mk)
        self.assertEqual((onnistuiko, self.kp.edulliset, self.kp.kassassa_rahaa, self.mk.saldo), (True, 1, 100000, 760))
    
    def test_kortilla_tarpeeksi_rahaa_maukas(self):
        onnistuiko = self.kp.syo_maukkaasti_kortilla(self.mk)
        self.assertEqual((onnistuiko, self.kp.maukkaat, self.kp.kassassa_rahaa, self.mk.saldo), (True, 1, 100000, 600))
    
    def test_kortilla_ei_tarpeeksi_rahaa_edullinen(self):
        self.mk.ota_rahaa(900)
        onnistuiko = self.kp.syo_edullisesti_kortilla(self.mk)
        self.assertEqual((onnistuiko, self.kp.edulliset, self.kp.kassassa_rahaa, self.mk.saldo), (False, 0, 100000, 100))

    def test_kortilla_ei_tarpeeksi_rahaa_maukas(self):
        self.mk.ota_rahaa(900)
        onnistuiko = self.kp.syo_maukkaasti_kortilla(self.mk)
        self.assertEqual((onnistuiko, self.kp.maukkaat, self.kp.kassassa_rahaa, self.mk.saldo), (False, 0, 100000, 100))

    def test_lataa_rahaa_kortille(self):
        self.kp.lataa_rahaa_kortille(self.mk, 1000)
        self.assertEqual((self.kp.kassassa_rahaa, self.mk.saldo),(101000, 2000))
    
    def test_lataa_rahaa_kortille_negatiivinen(self):
        self.kp.lataa_rahaa_kortille(self.mk, -1000)
        self.assertEqual((self.kp.kassassa_rahaa, self.mk.saldo),(100000, 1000))

   