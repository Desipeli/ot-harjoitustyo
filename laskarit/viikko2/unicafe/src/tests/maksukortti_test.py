import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahaa_voi_laittaa_kortille(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    #def test_negatiivinen_lisays_ei_vahenna_saldoa(self):
    #    self.maksukortti.lataa_rahaa(-5000)
    #    self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_otto_toimii_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_palauta_true_jos_raha_riittaa(self):
        arvo = self.maksukortti.ota_rahaa(500)
        self.assertEqual(arvo, True)
    
    def test_palauta_false_jos_rahat_eivat_riita(self):
        arvo = self.maksukortti.ota_rahaa(50000)
        self.assertEqual(arvo, False)
    
    def test_kortilta_kaikki_rahat_pois(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")