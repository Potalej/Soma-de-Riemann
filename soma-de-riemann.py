def integrar(funcao, intervalo, qntParticoes=10**5):
    '''Calcula a integral definida de uma função num dado intervalo e com uma dada quantidade de partições.'''

    deltaX = (intervalo[1]-intervalo[0])/qntParticoes
    soma = 0

    for iterador in range(qntParticoes+1):
        xi = intervalo[0] + deltaX*iterador
        fxi = funcao(xi)
        soma += fxi*deltaX

    return soma