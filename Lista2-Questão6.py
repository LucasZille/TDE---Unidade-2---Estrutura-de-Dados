import numpy as np
class ListatedSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.array(self.capacidade)

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i 
        return 'Não tem esse item na lista'  

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor         

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
        self.ultima_posicao -= 1       

    def imprime(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
