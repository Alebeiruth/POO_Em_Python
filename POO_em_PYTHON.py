class Empregado:
    def __init__(self, nome, CPF, RG):
        self.nome = nome
        self.CPF = CPF
        self.RG = RG

    def pagamento(self):
        print("Pagamento feito para o funcionario!")
        return 0

class EmpregadoHorista(Empregado):
    def __init__(self, nome, CPF, RG, horasTrabalhadas, pagamentoPorHora):
        Empregado.__init__(self, nome, CPF, RG)
        self.horasTrabalhadas = horasTrabalhadas
        self.pagamentoPorHora = pagamentoPorHora

    def pagamento(self):
        return self.horasTrabalhadas * self.pagamentoPorHora

class EmpregadoCLT(Empregado):
    def __init__(self, nome, CPF, RG, salario):
        Empregado.__init__(self, nome, CPF, RG)
        self.salario = salario

    def pagamento(self):
        return 13.33333 * self.salario

class PrestadorServico(Empregado):
    def __init__(self, nome, CPF, RG, pagamentoAvulso):
        Empregado.__init__(self, nome, CPF, RG)
        self.pagamentoAvulso = pagamentoAvulso

    def pagamento(self):
        return self.pagamentoAvulso
    