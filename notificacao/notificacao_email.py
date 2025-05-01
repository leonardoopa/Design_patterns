from abc import ABC, abstractmethod
from notificacao.notificacao import Notificacao


class NotificacaoEmail(Notificacao, ABC):
    @abstractmethod
    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando e-mail para {cliente.nome}: {mensagem}")

        
