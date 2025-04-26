from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("Leonardo", "Rua 1")
item_1 = Item("Computador", 5000.00)
item_2 = Item("Celular", 2000.00)

itens_pedido = [item_1, item_2]

taxa_entrega = 10.00
pedido_retirada = PedidoRetirada(cliente, itens_pedido)
pedido_delivery = PedidoDelivery(cliente, itens_pedido, taxa_entrega)

print(f"Total: R$ {pedido_delivery.calcular_total():.2f}")
