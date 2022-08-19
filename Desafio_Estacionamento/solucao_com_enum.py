from enum import Enum

class TipoVeiculo(Enum):
    CARRO = 1
    MOTO = 2

class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo

    def obterTipo(self):
        return self.tipo

    def __eq__(self, other):
        if other is None:
            return False
        if self.placa != other.placa:
            return False
        if self.tipo != other.tipo:
            return False
        return True

class Carro(Veiculo):
    def __init__(self, placa):
        Veiculo.__init__(self, placa, TipoVeiculo.CARRO)

class Moto(Veiculo):
    def __init__(self, placa):
        Veiculo.__init__(self, placa, TipoVeiculo.MOTO)

class Vagas:
    def __init__(self, tipo1ou2, idVaga, tipo):
        self.tipo1ou2 = tipo1ou2
        self.idVaga = idVaga
        self.veiculo = None
        self.tipo = tipo

    def Livre(self):
        return self.veiculo == None

    def estacionar(self, veiculo):
        if veiculo.tipo == self.tipo:
            self.veiculo = veiculo
            return True
        else:
            return False

    def removerVeiculo(self):
        self.veiculo = None
        return self.veiculo

    def obterVeiculo(self):
        return self.veiculo

class Patio:
    def __init__(self, andares, numero_de_vagas):
        self.andares = 1
        self.vagas_por_tipo1ou2 = 25
        self.tipos1ou2 = numero_de_vagas / self.vagas_por_tipo1ou2
        self.vagasEstacionamento = set()
        self.vagasDisponiveis = []

        for tipo1ou2 in range(int(self.tipos1ou2)):
            for i in range(self.vagas_por_tipo1ou2):
                import random
                self.vagasDisponiveis.append(Vagas(tipo1ou2, i, random.choice(list(TipoVeiculo))))

    def estacionar(self, veiculo):
        for vaga in self.vagasDisponiveis:
            if vaga.estacionar(veiculo):
                return True
        return False

    def remover(self, veiculo):
        for vaga in self.vagasDisponiveis:
            if vaga.obterVeiculo() == veiculo:
                vaga.removerVeiculo()
                return True
        return False

class Estacionamento:
    def __init__(self, unico_andar, numero_de_vagas):
        self.todo_patio = []
        for i in range(unico_andar):
            self.todo_patio.append(Patio(i, numero_de_vagas))

    def estacionarVeiculo(self, veiculo):
        for patio in self.todo_patio:
            if patio.estacionar(veiculo):
                return True
        return False

    def finalizar(self, veiculo):
        for patio in self.todo_patio:
            if patio.remover(veiculo):
                return True