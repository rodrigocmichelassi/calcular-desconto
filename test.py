import unittest
import calc

class TestSum(unittest.TestCase):

    ''' 
    Testar o comportamento da função quando o valor da compra é negativo
    '''
    def test_valor_compra_negativo(self):
        valor_compra = -1
        tipo_cliente = ""
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom), 
            0, 
            "Should be 0"
        )

if __name__ == "__main__":
    unittest.main()