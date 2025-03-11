#Em Python, listas são estruturas de dados que permitem armazenar vários valores em uma única variável. Esses valores podem ser de tipos diferentes, como números, textos ou até outras listas. As listas são ordenadas, o que significa que a ordem dos itens é preservada, e mutáveis, ou seja, você pode modificar os itens da lista após ela ser criada.
#Características principais de uma lista:
#Ordenação: A ordem dos elementos na lista é mantida.
#Mutabilidade: Você pode adicionar, remover ou alterar elementos da lista.
#Indexação: Os elementos são acessados por índice (o primeiro elemento tem o índice 0, o segundo tem o índice 1, e assim por diante).
#Aceita diferentes tipos de dados: Uma lista pode conter números, strings, outras listas, ou qualquer tipo de dado.

"""Resumo:
As listas em Python permitem armazenar múltiplos valores.
São mutáveis (podem ser alteradas após a criação).
Os elementos são indexados (acessados por números que começam em 0).
Você pode adicionar, remover ou modificar os itens da lista facilmente."""

Exercícios: 

#Crie uma lista

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas

areas = [hall, kit, liv, bed, bath]
print(areas)

# Criar listas com diferentes tipos
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]


# Print areas
print(areas)

# Lista de listas
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50


# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
          ["bathroom", bath]
        ]


# Print out house
print(house)

"""Subdivida para conquistar

Imprima o segundo elemento da lista areas (ele tem o valor 11.25).
Crie um subconjunto e imprima o último elemento de areas, que é 9.50. Aqui faz sentido usar um índice negativo!
Selecione o número que representa a área da sala de estar (20.0) e imprima-o."""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


# Print out second element from areas
print(areas[1])


# Print out last element from areas
print(areas[-1])


# Print out the area of the living room
print(areas[5])


# O índice start será incluído, enquanto o índice end não será. No entanto, também há a opção de não especificar esses índices. Se você não especificar o índice start, o Python entenderá que você deseja iniciar a fatia no início da lista.

"""1. Use o fatiamento para criar uma lista, downstairs, que contém os primeiros 6 elementos de areas.
2. Crie upstairs, com os últimos elementos de 4 de areas. Desta vez, simplifique o fatiamento omitindo o índice end.
3. Imprima os sites downstairs e upstairs usando print().
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

#Subdivisão de listas de listas

F#aça um subconjunto da lista house para obter o float 9.5.

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]


# Subset the house list
house[4][1]


"""Substitua elementos de listas
Para substituir elementos da lista, você faz um subconjunto da lista e atribui novos valores ao subconjunto. Podemos selecionar elementos individuais ou alterar fatias inteiras da lista de uma só vez.
Neste e nos próximos exercícios, você continuará trabalhando na lista areas, que contém os nomes e as áreas dos diferentes cômodos de uma casa.
Atualize a área do banheiro para que seja 10.50 metros quadrados em vez de 9.50 usando indexação negativa.
Torne a lista areas mais moderna! Altere "living room" para "chill zone". Não use indexação negativa desta vez."""


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]


# Correct the bathroom area
areas[-1] = 10.50


# Change "living room" to "chill zone"
areas[4] = "chill zone"


print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5]


"""Amplie uma lista
Você pode alterar os elementos de uma lista, mas também pode adicionar elementos a ela. Para fazer isso, utilize o operador +: Você pode usar o operador +:"""
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

"""Você acabou de ganhar na loteria, incrível! Você decide construir um anexo à piscina e uma garagem. Você pode adicionar as informações à lista areas?
Use o operador + para colar a lista ["poolhouse", 24.5] no final da lista areas. Armazene a lista resultante como areas_1.
Amplie ainda mais areas_1 adicionando dados sobre a garagem. Adicione a string "garage" e o float 15.45. Nomeie a lista resultante como areas_2.+"""

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]


# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]


# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]


print (areas)
print (areas_1)
print (areas_2)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5]
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5]
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.45]


"""Exclua elementos de uma lista
Por fim, também podemos remover elementos de uma lista. Podemos fazer isso com a instrução del:
x = ["a", "b", "c", "d"]
del x[1]"""

"""Preste atenção: assim que removemos um elemento de uma lista, todos os índices dos elementos que vêm depois do item excluído são alterados!
Infelizmente, o valor que você ganhou na loteria não é tão grande assim e parece que a casa da piscina não vai acontecer. Você precisará removê-lo da lista. Você decide remover a string e o float correspondentes da lista areas."""

#Exclua a string e o float para "poolhouse" da lista areas.
#Imprima a lista atualizada do site areas.

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.5, 'garage', 15.45]


"""Funcionamento interno das listas
Alguns códigos foram fornecidos para você neste exercício: uma lista com o nome areas e uma cópia chamada areas_copy.
Atualmente, o primeiro elemento da lista areas_copy é alterado e a lista areas é impressa. Se você pressionar o botão executar código, verá que, embora tenha alterado areas_copy, a alteração também terá efeito na lista areas. Isso ocorre porque areas e areas_copy apontam para a mesma lista.
Se quiser evitar que as alterações em areas_copy também tenham efeito em areas, você terá de fazer uma cópia mais explícita da lista areas com list() ou usando [:].
Altere o segundo comando, que cria a variável areas_copy, de modo que areas_copy seja uma cópia explícita de areas. Após a edição, as alterações feitas em areas_copy não devem afetar areas. Envie a resposta para conferir."""


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]


# Change this command
areas_copy = list (areas)


# Change areas_copy
areas_copy[0] = 5.0


# Print areas
print(areas)
