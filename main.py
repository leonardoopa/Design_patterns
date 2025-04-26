from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_pix import PagamentoPix
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_factory import PagamentoFactory

cliente = Cliente("Leonardo", "Rua 1")
item_1 = Item("Computador", 5000.00)
item_2 = Item("Celular", 2000.00)

itens_pedido = [item_1, item_2]

taxa_entrega = 10.00
pedido_retirada = PedidoRetirada(cliente, itens_pedido)
pedido_delivery = PedidoDelivery(cliente, itens_pedido, taxa_entrega)


valor_pedido = pedido_delivery.calcular_total()

# pagamento_cartao = PagamentoCartao().processar(valor_pedido)
# pagamento_pix = PagamentoPix()
# pagamento_pix.processar(valor_pedido)

tipo_pagamento = "cartao"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido)
