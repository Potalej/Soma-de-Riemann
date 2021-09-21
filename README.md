# Soma de Riemann

O cálculo de integrais definidas através de aproximações com somas de Riemann é dado, de forma geral, pelo seguinte limite:

![formula](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Cint_a%5Ebf%28x%29dx%3D%5Clim_%7B%5Cmax%5CDelta%20x_i%20%5Crightarrow%200%7D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7Df%28x_i%29%5CDelta%20x_i)

Onde o ![formula](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5CDelta%20x_i%20%3D%20x_i%20-%20x_%7Bi-1%7D). Ou seja, se a maior diferença tender a zero, a aproximação será boa. Tratando de forma computacional, a diferença nunca será nula, mas pode se aproximar conforme o tamanho de n. Assim, pode-se entrar com uma função, um intervalo e a quantidade de partições que se deseja usar:

```python
intervalo = [-1, 1]
funcao = lambda x: x**2
qntParticoes = 250

integral = integrar(funcao, intervalo, qntParticoes)
print(integral)
```

Neste caso, se utilizará 250 partições, a função x² e x estará compreendido entre os valores de -1 e 1. Calculando-se a integral definida usando métodos de integração, se tem:

![formula](https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Cint_%7B-1%7D%5E%7B1%7Dx%5E2dx%3D%5Cdfrac%7Bx%5E3%7D%7B3%7D%7C_%7B-1%7D%5E1%3D%5Cdfrac%7B1%5E3%7D%7B3%7D-%5Cdfrac%7B%28-1%29%5E3%7D%7B3%7D%3D%5Cdfrac%7B2%7D%7B3%7D%5Capprox%200.66667)

Já nas condições dadas, o programa retorna:
```terminal
0.6746879999999997
```

O que não é uma aproximação boa, mas se aumentando a quantidade de partições para 100 mil, tem-se:

```terminal
0.6666866667999961
```

O que já é um pouco melhor. 

Por padrão, a quantidade de partições é setada em 100 mil.
