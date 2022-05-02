from typing import Dict, List
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from IPython import embed
from interfaces import Conta
from mensagens import Mensagens

APP = Flask(__name__)
API = Api(APP)

PARSER = reqparse.RequestParser()
PARSER.add_argument('saque', type=float)
PARSER.add_argument('valor', type=float)
PARSER.add_argument('saldo_inicial', type=float)

CONTAS = {
    'conta1': Conta(1, 300.0),
    'conta2': Conta(2, 750.99),
    'conta3': Conta(3, 70.50),
}


def conta_existe(id: int, contas: List[Dict]) -> bool:
    key = f'conta{id}'
    return contas.get(key) != None


def get_conta(id: int, contas: List[Dict]) -> Conta:
    return contas.get(f'conta{id}')


def get_max_id(contas: List[Dict]) -> int:
    return max(list(map(lambda x: int(x.split('conta')[1]), contas)))


class Contas(Resource):
    def get(self):
        return [data.__dict__ for _, data in CONTAS.items()]

    def post(self):
        id = get_max_id(CONTAS) + 1
        CONTAS[f'conta{id}'] = Conta(id, 0.0)

        return CONTAS[f'conta{id}'].__dict__


class ContaResource(Resource):
    def get(self, id: int):
        if conta_existe(id, CONTAS):
            return get_conta(id, CONTAS).__dict__

        return Mensagens.INEXISTENTE(id)

    def delete(self, id: int):
        if conta_existe(id, CONTAS):
            CONTAS.pop(f'conta{id}')
            return Mensagens.REMOVIDO(id)

        return Mensagens.INEXISTENTE(id)

    def patch(self, id: int):
        response = Mensagens.INEXISTENTE(id)

        if conta_existe(id, CONTAS):
            args = PARSER.parse_args()
            conta = get_conta(id, CONTAS)
            
            saque = args['saque']
            valor = args['valor']

            if saque == True:
                response = conta.saque(valor)
            else:
                response = conta.deposito(valor)

        return response


@APP.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, Content-Type')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, PUT, PATCH, POST, DELETE')
    return response


RESOURCES = [
    (Contas, '/contas'),
    (ContaResource, '/contas/<int:id>'),
]

if __name__ == '__main__':
    for resource, endpoint in RESOURCES:
        API.add_resource(resource, endpoint)

    APP.run(debug=True)
