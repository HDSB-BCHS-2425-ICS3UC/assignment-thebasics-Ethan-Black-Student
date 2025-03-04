
import math

"""

#Basic Math

#Addition Practice
sum_add = 2 + 14
#Subtraction Practice
diffrerence = 2 - 14
#Multiplication Practice
product = 3 * 7
#Division Practice
quotient = 24 / 6
#Square Root Practice
sqaure = math.sqrt(9)
#Exponent Practice
exponent = 3**2
print (str(sum_add) + " " + str(diffrerence) + " " + str(product) + " " + str(quotient) + " " + str(sqaure) + " " + str(exponent))
print (" ")

#Tileable Discriminant

#Difine "a" Value
print ("Input a value")
a = int(input())
#Difine "b" Value
print ("Input b value")
b = int(input())
#Difine "c" Value
print ("Input c value")
c = int(input())
#Discriminent Equation
An = b**2-4*a*c
print (str("the Discriminant is ") + str(An))
print (" ")

"""

#3D Volume Calculator

print ()

while True:

    print ("My 3D Volume Calculator")
    print ()
    print ("What shape would you like to calculate the volume of?")
    print ("Prism, Sphere, Cone, or Cylinder?")
    print ()
    shape = str(input())
    print ()
    if (shape == "Prism"):
        print ("Triangular, Rectangular, or Cuboid?")
        print ()
        prism = str(input())
        print ()
        if (prism == "Triangular"):
            #Difine Base Value
            b = float(input("Base value is "))
            print ()
            #Difine Height Value
            h = float(input("Height value is "))
            print ()
            #Difine Length Value
            l = float(input("Length value is "))
            print ()
            v = 0.5*b*h*l
            print (str("The volume is "), float(v))
        if (prism == "Rectangular"):
            #Difine length Value
            l = float(input("Length value is "))
            print ()
            #Difine Width Value
            w = float(input("Width value is "))
            print ()
            #Difine Height Value
            h = float(input("Height value is "))
            print ()
            v = l*w*h
            print (str("The volume is "), float(v))
        if (prism == "Cuboid"):
            #Difine Side Length Value
            sl = float(input("Length value is "))
            print ()
            v = sl**3
            print (str("The volume is "), v)
    if (shape == "Sphere"):
        #Difine Radius Value
        r = float(input("Radius value is "))
        print ()
        v = (4/3)*math.pi*r**3
        print (str("The volume is "), float(v))
    if (shape == "Cone"):
        #Difine Radius Value
        r = float(input("Radius value is "))
        print ()
        #Difine Height Value
        h = float(input("Height value is "))
        print ()
        v = (h/3)*math.pi*r**2
        print (str("The volume is "), float(v))
    if (shape == "Cylinder"):
        #Difine Radius Value
        r = float(input("Radius value is "))
        print ()
        #Difine Height Value
        h = float(input("Height value is "))
        print ()
        v = h*math.pi*r**2
        print (str("The volume is "), float(v))
    
    print ()
    print ("Would you like to continue?")
    print ("Yes or No")
    print ()
    Continue = str(input())
    if (Continue == "No"): 
        print ()
        print (str("Thank you for using my volume calculator!"))
        print ()
        break
    if (Continue == "Yes"):
        print ()