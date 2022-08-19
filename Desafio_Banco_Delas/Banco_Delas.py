class Conta:
      def __init__(self, titular, saldo, saque, deposito):
    self.titular = []
    self.saldo = saldo
    self.saque = saque
    self.deposito = deposito

  #def saque(self, valor):
   # if self.saldo >= valor:
    #  self.saldo −= valor
    #  self.saque += valor
    # else:
    #  print("Saldo insuficiente")


  def deposito (self, valor):
    self.saldo += valor
    self.deposito += valor

    @property
    def renda_mensal(self):
      return self.saldo
    
    @saldo.sacar
    def sacar(self):
      self.saldo -saque
      return saldo
    
    @saldo.depositar
    def depositar(self):
      self.saldo +deposito
      return saldo

class Cliente:
  def __init__(self, mulher, nome, telefone, renda_mensal):
    self.mulher = True
    self._nome = nome
    self._telefone = telefone
    self.renda_mensal = renda_mensal

    def limite(self):
     if self.mulher == True:
        limite = renda_mensal
     else:
        limite == 0

    def saque(self, valor):
      if self.mulher == True:
        self.saldo + self.limite >= valor
        self.saque += valor
      if self.muler == False:
        if self.saldo >= valor:
          self.saldo =- valor
          self.saque += valor
      else:
        print("Saldo insuficiente")


#print(f"Boa tarde, {nome} seu Saldo é de: {saldo}")