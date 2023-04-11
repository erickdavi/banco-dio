transacoes = []
saldo = 0.00
LIMITE_DIARIO = 500.00

def deposito(valor):
    global transacoes
    global saldo
    saldo += valor
    transacoes.append({'operacao': 'd', 'valor': valor})

def saque(valor):
    global transacoes
    global saldo
    if(valor <= LIMITE_DIARIO):
      saldo -= valor
      transacoes.append({'operacao': 's', 'valor': valor})
    else:
      transacoes.append({'operacao': 'i', 'valor': 0.00})

deposito(5000.00)
saque(500)
saque(600)
print(f"{saldo}")
print(f"{transacoes}")