from abc import ABC, abstractmethod
from notificacao.notificacao import Notificacao


class NotificacaoSMS(Notificacao, ABC):
    @abstractmethod
    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando SMS para {cliente.nome}: {mensagem}")
