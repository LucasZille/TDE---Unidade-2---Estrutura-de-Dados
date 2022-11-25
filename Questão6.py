def TPilha(vetor):
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            pilha.empilhar(vetor[i])
        else:
            pilha.desempilhar()
