import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataus_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_rahan_otto(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_raha_ei_muutu_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_raha_riittää(self):
        self.assertEqual(self.maksukortti.ota_rahaa(3), True)
    
    def test_raha_ei_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)   