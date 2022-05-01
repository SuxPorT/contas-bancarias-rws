# T1 - Contas Bancárias - RWS

Construa, usando Python e a infraestrutura Flask-RESTful, um serviço de Contas Bancárias com a seguinte API:

## MÉTODO URL DESCRIÇÃO

- GET http://localhost:5000/contas -> obtém lista de contas
- GET http://localhost:5000/contas/ -> <id> obtém saldo da conta <id>
- POST http://localhost:5000/contas -> cria conta com identificador <id>
- PUT (ou PATCH) http://localhost:5000/contas/<id> -> efetua depósito/saque na conta <id>
- DELETE http://localhost:5000/contas/<id> -> deleta a conta <id>

O formato das mensagens JSON é livre. Teste as operações do seu serviço usando um cliente curl ou um programa Python (biblioteca requests).

Poste aqui o seu programa Python que implementa o serviço usando o Flask-RESTful.
