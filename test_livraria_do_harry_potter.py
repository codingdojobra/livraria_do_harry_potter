import unittest

def calcula_valor(listinha):
    descontos = {
        2: 0.95,
        3: 0.9,
        4: 0.85,
        5: 0.8,
    }

    valor = listinha[0]*listinha[1]*42*descontos[listinha[1]]
    valor += listinha[2]*listinha[3]*42*descontos[listinha[3]]
    return valor

def calcula_melhor_desconto(livros):
    lista_valores = []
    for n_livro in range(1, 6):
        for conjunto in [2, 3, 4, 5]:
            for n_livro2 in range(1, 6):
                for conjunto2 in [2, 3, 4, 5]:
                    if n_livro* conjunto + n_livro2 * conjunto2 == livros:
                        listinha = [n_livro,conjunto, n_livro2, conjunto2]
                        #lista_maior.append(listinha)
                        lista_valores.append(calcula_valor(listinha))
    return min(lista_valores)

class TestLivraria(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_8_livros(self):
        total_livros = 8
        valor_total = 281.40
        self.assertEqual(valor_total, calcula_melhor_desconto(total_livros))

if __name__ == '__main__':
    unittest.main()
