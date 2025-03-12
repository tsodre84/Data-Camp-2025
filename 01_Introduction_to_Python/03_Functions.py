"""Em Python, uma função é um bloco de código reutilizável que realiza uma tarefa específica. Ela pode receber dados de entrada (chamados de parâmetros), processá-los e, em seguida, retornar um resultado (ou não retornar nada). As funções ajudam a organizar e simplificar o código, permitindo que você execute a mesma tarefa em várias partes do programa sem precisar escrever o mesmo código repetidamente."""

fam = [1.73, 1.55, 1.69, 2.00]

# Encontrando o valor máximo na lista
maior_valor = max(fam)

# Imprimindo o valor máximo
print(maior_valor) 


# Exemplo de arredondamento com round()

# Número com várias casas decimais
numero = 3.14159

# Arredondando para 2 casas decimais
numero_arredondado = round(numero, 2)

# Imprimindo o número arredondado
print(f"O número {numero} arredondado para 2 casas decimais é {numero_arredondado}")


#ExemploFamiliar functions
"""Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). There are also functions like str(), int(), bool() and float() to switch between data types. You can find out about them here. These are built-in functions as well.
Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:
result = type(3.0)""
"Instructions
Use print() in combination with type() to print out the type of var1.
Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
Use int() to convert var2 to an integer. Store the output as out2"""

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2) # O valor True é convertido para 1 em Python quando passado para a função int(). Portanto, out2 será 1.

# Printing the result
print(out2)

"""Multiple arguments
In the previous exercise, you identified optional arguments by viewing the documentation with help(). You'll now apply this to change the behavior of the sorted() function.

Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

You'll see that sorted() takes three arguments: iterable, key, and reverse. In this exercise, you'll only have to specify iterable and reverse, not key.

Two lists have been created for you.

Can you paste them together and sort them in descending order?"""

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True) # This sorts the full list in descending order (largest to smallest). 

# Print out full_sorted
print(full_sorted)