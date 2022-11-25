class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.__valores = np.empty(self.capacidade, dtype = int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return
        
        if self.numero_elementos == 0:
            self.__valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.__valores[x]:
                    self.__valores[x + 1] = self.__valores[x]
                else:
                    break      
                x -= 1 

            self.__valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        
        valor = self.__valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor
