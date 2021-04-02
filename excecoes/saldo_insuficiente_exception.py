class SaldoInsuficienteException(Exception):
    def __init__(self):
        super().__init__("O Usuario nao possui o saldo necessario")