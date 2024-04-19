from datetime import date

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, cliente, numero, agencia=None):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    def nova_conta(cliente, numero, agencia=None):
        return Conta(cliente, numero, agencia)

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor
        return True

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            return True
        else:
            return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limites_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limites_saques = limites_saques

# Exemplo de uso:

# Criando um cliente
cliente1 = Cliente("Rua Principal, 123")

# Criando uma conta corrente para o cliente
conta1 = Conta.nova_conta(cliente1, 1001)

# Adicionando a conta ao cliente
cliente1.adicionar_conta(conta1)

# Realizando um depósito de R$ 500,00 na conta
deposito1 = Deposito(500.0)
cliente1.realizar_transacao(conta1, deposito1)

# Realizando um saque de R$ 200,00 na conta
saque1 = Saque(200.0)
cliente1.realizar_transacao(conta1, saque1)

# Verificando o saldo atual da conta
print("Saldo atual da conta:", conta1.saldo)
