from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        """defina na clsse filha"""

    @abstractmethod
    def andar(self):
        """defina na clsse filha"""


        class Cachorro(IAnimal):
            
            def falar(self):
                print("AuAu")

            def andar(self):
                print("ando com 4 patas")


        class Pessoas:

            
            def __init__(self, nome, idade):
                self._nome = nome
                self.idade = idade
                self.__humano = True

            def falar_pessoas(self):
                print("Falando")

            def mostra_nome_e_idade(self):
                print(f"Nome: {self._nome} e Idade: {self.idade}")


# animal = IAnimal()
pingo = Cachorro()
pingo.fala()
pingo.andar()

humano = Pessoa("Fulano", 35)
humano.fala_pessoa()
humano.mostra_nome_e_idade()

