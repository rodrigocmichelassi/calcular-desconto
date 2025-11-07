import unittest
import calc

class TestSum(unittest.TestCase):

    def test_valor_compra_negativo(self):
        valor_compra = -1
        tipo_cliente = ""
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom), 
            0, 
            "Compra inválida (sem valor ou negativa). (C1)"
        )

    def test_premium_scupom_staxa(self):
        valor_compra = 100
        tipo_cliente = "premium"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            85,
            "Cliente premium, sem cupom aplicável, valor suficiente para não cobrar taxa extra. (C2)"
        )

    def test_premium_ccupom_staxa(self):
        valor_compra = 150
        tipo_cliente = "premium"
        cupom = "DESC10"
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            112.5,
            "Cliente premium, usa cupom e a compra é grande o bastante; valor final continua acima de 50. (C3)"
        )

    def test_premium_scupom_ctaxa(self):
        valor_compra = 40
        tipo_cliente = "premium"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            39,
            "Cliente premium, sem cupom, valor pequeno — aplica taxa de entrega. (C4)"
        )

    def test_regular_scupom_staxa(self):
        valor_compra = 100
        tipo_cliente = "regular"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            95,
            "Cliente regular, sem cupom, valor suficiente. (C5)"
        )
    
    def test_regular_ccupom_staxa(self):
        valor_compra = 150
        tipo_cliente = "regular"
        cupom = "DESC10"
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            127.5,
            "Cliente regular, cupom “DESC10” aplicado, valor final ≥ 50. (C6)"
        )

    def test_regular_scupom_ctaxa(self):
        valor_compra = 40
        tipo_cliente = "regular"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            43,
            "Cliente regular, sem cupom, compra pequena, taxa de entrega aplicada. (C7)"
        )

    def test_outro_scupom_staxa(self):
        valor_compra = 100
        tipo_cliente = "outro"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            100,
            "Cliente “outro tipo”, sem desconto, sem taxa adicional. (C8)"
        )
    
    def test_outro_ccupom_staxa(self):
        valor_compra = 150
        tipo_cliente = "outro"
        cupom = "DESC10"
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            135,
            "Cliente sem categoria especial, cupom aplicado, valor ≥ 50. (C9)"
        )
    
    def test_outro_scupom_ctaxa(self):
        valor_compra = 40
        tipo_cliente = "outro"
        cupom = ""
        self.assertEqual(
            calc.calcular_desconto(valor_compra, tipo_cliente, cupom),
            45,
            "Cliente “outro tipo”, sem cupom, valor pequeno, taxa adicionada. (C10)"
        )

if __name__ == "__main__":
    unittest.main()