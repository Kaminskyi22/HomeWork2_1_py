num1=float(input("Enter number 1 :"))
num2=float(input("Enter number 2 :"))
num3=float(input("Enter number 3 :"))

sum=num1+num2+num3
mult=num1*num2*num3

c=(input("What you want to do with digits (1 = +, 2 = *)"))
match c:
    case 1 | "+":
        print(f"Total =  {sum}")
    case 2 | "*":
        print(f"Multiplication = {mult}")
    case _ : print ("Incorrectly selected action")
