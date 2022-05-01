from multiprocessing.sharedctypes import Value
import requests

API = 'http://localhost:5000/contas'


class Banco:
    def __init__(self, api_url: str):
        self._api = api_url

    def criar_conta(self) -> dict:
        return requests.post(url=self._api).json()

    def remover_conta(self, _id: int) -> dict:
        url = self._api + '/' + str(_id)
        return requests.delete(url=url).json()

    def listar_contas(self) -> dict:
        return requests.get(self._api).json()

    def saque(self, _id: int, valor: float) -> dict:
        url = f'{self._api}/{_id}'
        data = {'valor': valor, 'saque': True}
        return requests.put(url, json=data).json()

    def deposito(self, _id: int, valor: float) -> dict:
        url = f'{self._api}/{_id}'
        data = {'valor': valor, 'saque': False}
        return requests.put(url, json=data).json()

    def saldo(self, _id: int) -> dict:
        return requests.get(self._api + '/' + str(_id)).json()


def main() -> None:
    banco = Banco(API)

    operacoes = {
        'saque': banco.saque,
        'deposito': banco.deposito,
        'listar': banco.listar_contas,
        'saldo': banco.saldo,
        'criar': banco.criar_conta,
        'remover': banco.remover_conta,
        'sair': None
    }

    cmd = ''
    print('Bem-vindo(a) ao banco. Operações disponíveis:')
    print(' - '+'\n - '.join(i for i in operacoes))

    while cmd != 'sair':
        cmd = input('[ Banco ] ~ ')

        if cmd not in operacoes and cmd != 'exit':
            print(f'Comando "{cmd}" não existe.')
            continue

        _cmd = operacoes.get(cmd)
        if cmd == 'listar' or cmd == 'criar':
            resp = _cmd()
            print(resp)

        if cmd == 'saque' or cmd == 'deposito':
            try:
                _id = int(input('Conta: '))
                valor = float(input('Valor: '))
            except ValueError:
                print('Valor inválido')
                continue
            resp = _cmd(_id, valor)
            print(resp)

        if cmd == 'saldo' or cmd == 'remover':
            try:
                _id = int(input('Conta: '))
            except ValueError:
                print('Valor inválido')
                continue

            resp = _cmd(_id)
            print(resp)


if __name__ == '__main__':
    main()
