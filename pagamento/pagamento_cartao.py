from pagamento.pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Pagamento por cartão: R$ {valor:.2f}")
