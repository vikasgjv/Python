# Match Case Statements

x = int(input("Enter a number : "))

match x:
    case 0:
        print("number is zero")
    case 1:
        print("number is 1")
    case 6:
        print("number is 6")
    case _ if x==100:
        print("number is 100")
    case _:   #default
        print("the number is  : " ,x)
