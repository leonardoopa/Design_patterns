from pagamento.pagamento import Pagamento


class PagamentoPix(Pagamento):
    def processar(self, valor):
        print(f"Pagamento por PIX: R$ {valor:.2f}")
