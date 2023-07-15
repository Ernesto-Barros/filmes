
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
    def extrato(self):
        print("O saldo de {}  é de {}".format(self.__titular,self.__saldo))

    def deposita(self,valor):
        self.__saldo=self.__saldo+valor

    def __temDisponabilidade(self,valor_a_sacar):
        valor_disponivel=self.__saldo + self.__limite
        print(valor_disponivel)
        if (valor_a_sacar <= valor_disponivel):
            return True
        else:
            return False

    def saca(self,valor):
        if(self.__temDisponabilidade(valor)):
            self.__saldo = self.__saldo-valor
        else:
            print("você não tem limite disponível")

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite= limite




