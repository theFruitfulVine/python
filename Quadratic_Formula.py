#This python script will calculate the roots of an equation
#using the formular method

#(c) theFruitfulVine


import cmath
import math

print """\tSample Values
	real roots = 1,-5,2
	equal roots = 4,4,1
	complex roots = 5,3,1
	"""

def formular(a,b,c):
	#calculate the discriminant
	dis = (b ** 2) - (4 * a* c)

	if (dis > 0):
		root1 = ((- b) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
		root2 = ((- b) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
		print ("Equation %dx^2 + %dx + %d has two real roots") % (a,b,c)
		print ('root1 =  %1.2f and root2 = %1.2f') %(root1, root2) #This prints to two decimal places
		
	elif (dis == 0):
		root = (- b) / (2 * a)
		print ("Equation %dx^2 + %dx + %d has two equal roots") % (a,b,c)
		print ('root = %1.2f') %(root) #This prints to two decimal places
	
	else:
		root1 = ((- b) + cmath.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
		root2 = ((- b) - cmath.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
		print ("Equation %dx^2 + %dx + %d has two complex roots") % (a,b,c)
		print ('root1 = {:.2f} and root2 = {:.2f}'.format(root1, root2)) #This prints to two decimal places
		
a = float(raw_input("Enter the coeficient of x^2: "))
b = float(raw_input("Enter the coeficient of x: "))
c = float(raw_input("Enter the constant: "))

roots = formular(a,b,c)
