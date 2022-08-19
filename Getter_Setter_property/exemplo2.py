class Adulto:
  def __init__(self):
    self._idade = 0

  @property
  def idade(self):
    print ("getter method called")
    return self._idade

  @idade.setter
  def idade(self, x):
    if x < 18:
      raise ValueError("Desculpe, você não atendeu os critérios. Portanto não é Adulto.")
    print("setter method called")
    self._idade = x

marcos = Adulto()

marcos.idade = 19

print(marcos.idade)