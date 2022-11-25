def pilhasiguais(pilha1, pilha2):
    igual = True
    indice = 0;
    if len(pilha1) != len(pilha2):
        igual = False
        
    while (indice < len(pilha1)):
        if pilha1[indice] == pilha2[indice]:
            indice += 1
        else:
            igual = False
            break

    if igual == True:
        print('A pilha é igual')
    else:
        print('A pilha não é igual')
