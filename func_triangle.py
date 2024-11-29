'''
Author:Athul George
Discription:
program that accepts the lengths of three sides of a triangle
 as inputs. The program should output whether or not the triangle is
 a right triangle (Recall from the Pythagorean Theorem that in a right triangle,
 the square of one side equals the sum of the squares of the other two sides).
Implement using functions.
'''



side1=int(input("Enter the first side:"))
side2=int(input("Enter the second side:"))
side3=int(input("Enter the third side:"))

def triangle(side1,side2,side3):
    x = [side1, side2, side3]
    x.sort()
    if x[0]**2 + x[1]**2 == x[2]**2:
        print("It's a right angled triangle")
    else:
        print("Its not a right triangle")

triangle(side1 ,side2, side3)