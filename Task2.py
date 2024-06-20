num1=float(input("Enter number 1 :"))
num2=float(input("Enter number 2 :"))
num3=float(input("Enter number 3 :"))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)

# print(f"Max number = {max_num}")
# print(f"Min number = {min_num}")
c=(input("What you want to do with digits (1 = max, 2 = min)"))
match c:
    case 1 | "max":
        print(f"Max number = {max_num}")
    case 2 | "min":
        print(f"Min number = {min_num}")
    case _ : print ("Incorrectly selected action")