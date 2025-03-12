"""Em Python, métodos são funções que estão associadas a um objeto específico. 
Eles são definidos dentro de uma classe e são usados para realizar operações ou ações 
relacionadas ao objeto. 
Métodos permitem que você interaja com os dados de um objeto e modifique seu comportamento."""


"""Use the .upper() method on place and store the result in place_up. 
Use the syntax for calling methods that you learned in the previous video.
Print out place and place_up. Did both change?
Print out the number of o's on the variable place by calling .count() on place and 
passing the letter 'o' as an input to the method. 
We're talking about the variable place, not the word "place"!"""

# String to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)   # Original string
print(place_up)  # String in uppercase

# Print out the number of 'o's in place
num_o = place.count('o')  # Counting 'o' characters in 'place'
print(f"The number of 'o's in place is: {num_o}")

"""List Methods
Strings are not the only Python types that have methods associated with them. Lists, floats, 
integers and booleans are also types that come packaged with a bunch of useful methods. 
In this exercise, you'll be experimenting with:

.index(), to get the index of the first element of a list that matches its input and
.count(), to get the number of times an element appears in a list.
You'll be working on the list with the area of different parts of a house: areas.

Use the .index() method to get the index of the element in areas that is equal to 20.0. 
Print out this index.
Call .count() on areas to find out how many times 9.50 appears in the list. 
Again, simply print out this number.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))  # Output: 2

# Print out how often 9.50 appears in areas
print(areas.count(9.50))  # Output: 1

"""List Methods (2)
Most list methods will change the list they're called on. Examples are:

.append(), that adds an element to the list it is called on,
.remove(), that removes the first element of a list that matches the input, and
.reverse(), that reverses the order of the elements in the list it is called on.
You'll be working on the list with the area of different parts of the house: areas.

Use .append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, 
respectively. Make sure to add them in this order.
Print out areas
Use the .reverse() method to reverse the order of the elements in areas.
Print out areas once more.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)  # Add poolhouse size
areas.append(15.45)  # Add garage size

# Print out areas
print(areas)  # Output: [11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]

# Reverse the order of the elements in areas
areas.reverse()

# Print out areas
print(areas)  # Output: [15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]

