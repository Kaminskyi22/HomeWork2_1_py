metr=float(input("Enter the distance in meters: "))
km=metr/1000
mile=metr/1609
inch=metr/39.37
yard=metr/1.094

c=(input("What you want to convert (1 = km, 2 = mile, 3 = inch, 4 = yard)"))
match c:
    case 1 | "km":
        print(f"Distance in kilometers =  {km}")
    case 2 | "mile":
        print(f"Distance in miles = {mile}")
    case 3 | "inch":
        print(f"Distance in inches = {inch}")
    case 4 | "yard":
        print(f"Distance in yards = {yard}")
    case _ : print ("Incorrectly selected action")
