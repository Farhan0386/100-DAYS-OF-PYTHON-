import math
name=input("What's your Sweat Name  :")

print("WELCOME", name)

print("This is a program to find dimension of square and cube\nAnd the author of this program is Farhan Hussain")

#lets give a variable to side of square and cube

a=float(input("Please Enter the Side of Square or Cube :")) # here we use typecasting float to gain more detail about side

print("The  Parameter of Square : ",  4*a)

print("The Area of Square : ",   a**2)

print("The Daignol of Square : ",a*math.sqrt(2))

print("If", a ,"is Side of Cube THEN")

print("The volume of Cube :",  a**3)

print("The Total suface area of Cube : ",   6*(a**2))

print("The curved surface area of cube : ",  4*(a**2))

print("the Daignol of cube :",    a*math.sqrt(3))

print("Thankyou so much for using this program\nThis program is under Devlopment")
