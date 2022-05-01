from mensagens import Mensagens


class Conta:
    def __init__(self, id: int, saldo: float):
        self.id = id
        self.saldo = saldo

    def deposito(self, valor):
        resp = Mensagens.VALOR_INVALIDO(valor)
        if valor:
            self.saldo += valor
            resp = Mensagens.TRANSACAO_VALIDA()
        return resp

    def saque(self, valor):
        if not self.saldo:
            return Mensagens.SALDO_INVALIDO(self.id)

        if not valor:
            return Mensagens.VALOR_INVALIDO(valor)

        self.saldo -= valor
        return Mensagens.TRANSACAO_VALIDA()
