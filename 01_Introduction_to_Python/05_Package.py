"""Import package
Let's say you wanted to calculate the circumference and area of a circle.
 Here's what those formulas look like:
C=π2r
a=πr**2
Rather than typing the number for pi, you can use the math package that contains the number

For reference, ** is the symbol for exponentiation. For example 3**4 is 3 
to the power of 4 and will give 81.

Import the math package.
Use math.pi to calculate the circumference of the circle and store it in C.
Use math.pi to calculate the area of the circle and store it in A.
"""

# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))


"""Selective import
General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

from math import pi
Try the same thing again, but this time only use pi.

Perform a selective import from the math package where you only import the pi function.
Use math.pi to calculate the circumference of the circle and store it in C.
Use math.pi to calculate the area of the circle and store it in A.
"""

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

"""Different ways of importing
There are several ways to import packages and modules into Python. Depending on the import call,
 you'll have to use different Python code.

Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package.
You want to be able to use this function as follows:

    my_inv([[1,2], [3,4]])

Which import statement will you need in order to run the above code without an error?"""