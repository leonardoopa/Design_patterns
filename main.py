from cliente import Cliente 
from item import Item 

item_1 = Item("Computador", 5000)
print(f"{item_1.nome} esta custando {item_1.preco}")

item_2 = Item("Celular", 2000)
print(f"{item_2.nome} esta custando {item_2.preco}")

cliente = Cliente("Leonardo", "Rua 1")
print(f"{cliente.nome} mora na {cliente.endereco}")
