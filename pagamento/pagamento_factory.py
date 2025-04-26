from pagamento.pagamento_pix import PagamentoPix
from pagamento.pagamento_cartao import PagamentoCartao


class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo_pagamento):
        if tipo_pagamento == "pix":
            return PagamentoPix()
        elif tipo_pagamento == "cartao":
            return PagamentoCartao()
        else:
            raise ValueError("Tipo de pagamento inválido")
