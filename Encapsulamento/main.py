class Pessoa:
      def __init__(self, nome, profissao, identidade):
    self._nome = nome
    self.profissao = profissao
    self.__identidade = identidade

  def __str__(self):
    return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa('Ana', 'Programadora', '123456')
print(pessoa1)

#Ao tentar alterar um atributo _protegido, o valor é alterado
pessoa1.profissao = 'Médica'
print(pessoa1)

#Ao tentar alterar um atributo __privado, o valor não vai ser alterado
pessoa1.__identidade = '222244'
print(pessoa1)

#Ao tentar alterar um atributo _protegido, vamos conseguir
pessoa1._nome = 'Roberta'
print(pessoa1)