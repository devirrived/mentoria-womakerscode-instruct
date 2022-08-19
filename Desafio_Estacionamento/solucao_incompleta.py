class Estacionamento:
      def __init__(self, vagas_carro, vagas_moto):
    self._vagas_carro = list(range(1, 25))
    self._vagas_moto = list(range(26, 50))



class Veiculo:
  def __init__(self, tipo, placa):
    self.tipo = tipo
    self.placa = placa
    self.estacionado = False

  def estacionar(self):
    self.estacionado = True
    print(f'{self.tipo} está estacionado')

  def remover(self):
    self.estacionado = False
    print(f'{self.tipo} saiu da vaga')

class Carro(Veiculo):
  def __init__(self, tipo, placa):
    super().__init__(tipo, placa)

class Moto(Veiculo):
  def __init__(self, tipo, placa):
    super().__init__(tipo, placa)