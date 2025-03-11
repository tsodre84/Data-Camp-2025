#O que são variáveis em Python?
#Variáveis em Python são "caixas" que usamos para armazenar informações, como números, textos ou outros tipos de dados. Cada variável tem um nome e pode armazenar diferentes tipos de valores. Quando você cria uma variável, está basicamente dizendo: "Eu quero guardar um valor com esse nome para usá-lo mais tarde no programa."

#Armazenando um número:
idade = 25  # A variável "idade" armazena o número 25
print(idade)  # Isso imprime o valor de "idade", que é 25

#Armazenando um texto (string):
nome = "João"  # A variável "nome" armazena o texto "João"
print(nome)  # Isso imprime o valor de "nome", que é "João"

#Armazenando um valor booleano (verdadeiro ou falso):
eh_maior_de_idade = True  # A variável "eh_maior_de_idade" armazena o valor True
print(eh_maior_de_idade)  # Isso imprime True

#Armazenando uma lista de valores:
frutas = ["maçã", "banana", "laranja"]  # A variável "frutas" armazena uma lista
print(frutas)  # Isso imprime a lista de frutas

"""Resumo:
Uma variável pode armazenar diferentes tipos de dados (números, textos, listas, etc.).
Você escolhe um nome para a variável, que deve ser único e descritivo.
Uma vez que a variável é criada, você pode usar o valor armazenado nela sempre que precisar."""

#Em Python, você pode usar a função type() para verificar o tipo de dado de uma variável. A função type() retorna o tipo da variável que você passar como argumento.

# Exemplo 1: Número inteiro
x = 10
print(type(x))  # Vai imprimir <class 'int'>, que significa que x é um número inteiro (int)

# Exemplo 2: Texto (string)
nome = "Maria"
print(type(nome))  # Vai imprimir <class 'str'>, que significa que nome é uma string (str)

# Exemplo 3: Número com ponto flutuante (float)
preco = 19.99
print(type(preco))  # Vai imprimir <class 'float'>, que significa que preco é um número decimal (float)

# Exemplo 4: Lista
frutas = ["maçã", "banana", "laranja"]
print(type(frutas))  # Vai imprimir <class 'list'>, que significa que frutas é uma lista (list)

"""Tipos de dados comuns em Python:
int: para números inteiros (exemplo: 10, -3, 0)
float: para números decimais (exemplo: 10.5, -3.14, 0.99)
str: para texto (strings) (exemplo: "Olá", "Python", "123")
bool: para valores lógicos (True ou False)
list: para listas de itens (exemplo: [1, 2, 3], ["maçã", "banana"])
dict: para dicionários (exemplo: {"nome": "João", "idade": 30})
Saídas esperadas:
<class 'int'>: significa que a variável é um número inteiro.
<class 'str'>: significa que a variável é uma string.
<class 'float'>: significa que a variável é um número de ponto flutuante.
<class 'list'>: significa que a variável é uma lista.
Essa função é muito útil para entender o tipo de dado que você está manipulando em seu código.""" 
