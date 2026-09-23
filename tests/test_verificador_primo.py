import unittest

from verificador_primo import eh_primo


class TestEhPrimo(unittest.TestCase):
    def test_primos_pequenos(self):
        for numero in (2, 3, 5, 7, 11, 13):
            with self.subTest(numero=numero):
                self.assertTrue(eh_primo(numero))

    def test_compostos(self):
        for numero in (4, 6, 8, 9, 10, 12, 15, 21):
            with self.subTest(numero=numero):
                self.assertFalse(eh_primo(numero))

    def test_valores_menores_que_dois(self):
        for numero in (-10, -1, 0, 1):
            with self.subTest(numero=numero):
                self.assertFalse(eh_primo(numero))

    def test_primos_maiores(self):
        self.assertTrue(eh_primo(97))
        self.assertTrue(eh_primo(9973))

    def test_multiplos_de_dois_e_tres(self):
        self.assertFalse(eh_primo(100))
        self.assertFalse(eh_primo(111))

    def test_numero_no_limite_da_raiz_quadrada(self):
        self.assertFalse(eh_primo(121))
        self.assertTrue(eh_primo(127))

    def test_rejeita_tipo_invalido(self):
        with self.assertRaises(TypeError):
            eh_primo("17")

        with self.assertRaises(TypeError):
            eh_primo(True)


if __name__ == "__main__":
    unittest.main()
