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
          
def addCarros():
    capacidade = int(input('Digite quantas placas você quer adicionar? '))
    global lista 
    lista = Pilha(capacidade)

    for i in range(capacidade):
        lista.empilhar(int(input('Digite as placas(Primeiro a entrar é o ultimo a sair): ')))

def pesquisaCarro(placa):
        CarrosSair = []
        pilha = list(reversed(lista.valores))
        if placa not in pilha:
            print('Veiculo não está estacionado')
        else:
            for i in range(len(pilha)):
                if placa == pilha[i]:
                    for j in range(i):
                        CarrosSair.append(pilha[j])

        print(f'Os proximos carros a sair são: {CarrosSair}')
