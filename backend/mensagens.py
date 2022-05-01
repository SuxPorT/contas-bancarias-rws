class Mensagens:
    def REMOVIDO(id): return {"message": f'conta {id} removida'}
    def INEXISTENTE(id): return {"message": f'conta {id} inexistente'}
    def SALDO_INVALIDO(id): return {"message": f'saldo da conta {id} invalido'}
    def VALOR_INVALIDO(id): return {"message": f'valor \'{id}\' invalido'}

    def VALOR_SACADO(id, valor): return {
        "message": f'valor \'{valor}\' sacado da conta {id}'}

    def TRANSACAO_VALIDA(): return {"message": "OK"}
