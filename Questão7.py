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

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A Pilha está cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia')
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1
  
p = Pilha(6)
n = Pilha(3)
def TPilhas2(n, p, vetor2):
    for i in range(len(vetor2)):
        if vetor2[i] < 0:
            n.empilhar(vetor2[i])
        elif vetor2[i] > 0:
            p.empilhar(vetor2[i])
            if vetor2[i] == 0:
                n.desempilhar()
                p.desempilhar()
