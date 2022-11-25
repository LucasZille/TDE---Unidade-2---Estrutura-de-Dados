import numpy as np
class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype = int)
    def __pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False
    def empilhar(self, vetor):
        self.vetor = vetor
        if self.__pilha_cheia():
            print('A Pilha está cheia.')
        else:
            for i in self.vetor:
                self.topo += 1
                temp = i
                self.valores[self.topo] = temp

pilha3 = Pilha(10)
pilha3.empilhar(vetor)
