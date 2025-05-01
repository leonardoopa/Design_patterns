class ObservaodorStatus:
    def __init__(self, notificacoes):
        self.notificacoes = notificacoes

    def atualizar(self, pedido):
        mensagem = f"Status atual: {pedido.status}"
        self.notificacoes.enviar_notificacoes(pedido.cliente, mensagem)
