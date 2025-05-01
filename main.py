from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservaodorStatus

cliente = Cliente("Leonardo", "Rua 1")
item_1 = Item("Computador", 5000.00)
item_2 = Item("Celular", 2000.00)

itens_pedido = [item_1, item_2]

taxa_entrega = 10.00
pedido = PedidoDelivery(cliente, itens_pedido, taxa_entrega)


valor_pedido = pedido.calcular_total()

tipo_pagamento = "cartao"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM = "Seu pedido foi realizado com sucesso!"
MENSAGEM_PREPARANDO = "O pedido esta sendo preparado!"
MENSAGEM_ENVIADO = "O pedido ja saiu pra entrega!"
MENSAGEM_ENTREGUE = "O pedido foi entregue!"
MENSAGEM_CANCELADO = "O pedido foi cancelado!"

notificacoes = NotificacaoFacade()
observador = ObservaodorStatus(notificacoes)
pedido.adicionar_observador(observador)

pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
pedido.status = MENSAGEM_ENTREGUE
