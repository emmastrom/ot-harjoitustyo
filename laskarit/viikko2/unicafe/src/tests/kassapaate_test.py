import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_lounaat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_lounaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)



    
    def test_edullisesti_kateisella_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullisesti_kateisella_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    
    def test_edullisesti_kateisella_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_ei_riita_syoda_edullisesti_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_ei_riita_syoda_edullisesti_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    def test_ei_riita_syoda_edullisesti_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)



    
    def test_maukkaasti_kateisella_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukkaasti_kateisella_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_maukkaasti_kateisella_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_ei_riita_syoda_maukkaasti_kateisella_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_ei_riita_syoda_maukkaasti_kateisella_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)
    
    def test_ei_riita_syoda_maukkaasti_kateisella_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.maukkaat, 0)



    
    def test_edullisesti_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_edullisesti_kortin_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")
    
    def test_edullisesti_kortilla_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_ei_riita_edullisesti_kortilla(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    
    def test_ei_riita_edullisesti_kortilla_saldo(self):
        self.maksukortti.ota_rahaa(300)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
    
    def test_ei_riita_edullisesti_kortilla_lounaiden_maara(self):
        self.maksukortti.ota_rahaa(300)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassassa_rahaa_edullisesti_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    def test_maukkaasti_kortilla_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukkaasti_kortin_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_maukkaasti_kortilla_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_ei_riita_maukkaasti_kortilla(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_ei_riita_maukkaasti_kortilla_saldo(self):
        self.maksukortti.ota_rahaa(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")
    
    def test_ei_riita_maukkaasti_kortilla_lounaiden_maara(self):
        self.maksukortti.ota_rahaa(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassassa_rahaa_maukkaasti_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    

    def test_lataa_kortille_rahaa_kortin_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
    
    def test_lataa_kortille_rahaa_kassan_rahat(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_lataa_kortille_negatiivinen_maara_kortin_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_lataa_kortille_negatiivnen_maara_rahaa_kassan_rahat(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)