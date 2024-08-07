class Pessoa:
    def _init_(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def calcular_ano_nascimento(self):
        from datetime import datetime
        ano_atual = datetime.now().year
        return ano_atual - self.__idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade