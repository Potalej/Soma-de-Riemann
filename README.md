# Soma de Riemann

O cálculo de integrais definidas através de aproximações com somas de Riemann é dado, de forma geral, pelo seguinte limite:

$$
  \int_a^b f(x)dx = \lim_{max \Delta x_i \rightarrow 0} \sum_{i=1}^n f(x_i) \Delta x_i
$$

Onde $\Delta x_i = x_i - x_{i-1}$. Ou seja, se a maior diferença tender a zero, a aproximação será boa. Tratando de forma computacional, a diferença nunca será nula, mas pode se aproximar conforme o tamanho de n. Assim, pode-se entrar com uma função, um intervalo e a quantidade de partições que se deseja usar:

```python
intervalo = [-1, 1]
funcao = lambda x: x**2
qntParticoes = 250

integral = integrar(funcao, intervalo, qntParticoes)
print(integral)
```

Neste caso, se utilizará 250 partições, a função x² e x estará compreendido entre os valores de -1 e 1. Calculando-se a integral definida usando métodos de integração, se tem:

$$
\int_{-1}^{1} x^2 dx = \dfrac{x^3}{3}|_{-1}^{1} = \dfrac{1^3}{3}-\dfrac{(-1)^3}{3} = \dfrac{2}{3} \approx 0.66667
$$

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
