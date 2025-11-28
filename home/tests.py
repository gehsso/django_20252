from django.test import TestCase

class Conta:
    def __init__(self,cliente,saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
  
conta_a = Conta('João',100)

print(conta_a.cliente);
conta_a.depositar(200)
print(conta_a.saldo)  # 300
conta_a.sacar(300)
print(conta_a.saldo)  # 0


print(conta_a.cliente);

print(f'CLIENTE A: {conta_a.cliente}');


class Aluno:
    pass

a1 = Aluno('888', 'José')
a1.adcionar_nota(7)
a1.adcionar_nota(8)
a1.adcionar_nota(9)
print(f'Aluno {a1.nome} - Média: {a1.media()}')
