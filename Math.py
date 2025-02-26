
import math

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
            print ()
            b = float(input("Base value is "))
            print ()
            #Difine Height Value
            print ()
            h = float(input("Height value is "))
            print ()
            #Difine Length Value
            print ()
            l = float(input("Length value is "))
            print ()
            v = 0.5*b*h*l
            print (str("The volume is "), float(v))
        if (prism == "Rectangular"):
            #Difine length Value
            print ()
            l = float(input("Length value is "))
            print ()
            #Difine Width Value
            print ()
            w = float(input("Width value is "))
            print ()
            #Difine Height Value
            print ()
            h = float(input("Height value is "))
            print ()
            v = l*w*h
            print (str("The volume is "), float(v))
        if (prism == "Cuboid"):
            #Difine Side Length Value
            print ()
            sl = float(input("Length value is "))
            print ()
            v = sl**3
            print (str("The volume is "), float(v))
    if (shape == "Sphere"):
        #Difine Radius Value
        print ()
        r = float(input("Radius value is "))
        print ()
        v = (4/3)*math.pi*r**3
        print (str("The volume is "), float(v))
    if (shape == "Cone"):
        #Difine Radius Value
        print ()
        r = float(input("Radius value is "))
        print ()
        #Difine Height Value
        print ()
        h = float(input("Height value is "))
        print ()
        v = (h/3)*math.pi*r**2
        print (str("The volume is "), float(v))
    if (shape == "Cylinder"):
        #Difine Radius Value
        print ()
        r = float(input("Radius value is "))
        print (" ")
        #Difine Height Value
        print ()
        h = float(input("Height value is "))
        print (" ")
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