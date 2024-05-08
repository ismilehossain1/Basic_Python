# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)

x= int(input("Enter the value of x: "))
print(x)
match x:
    case 0:
        print("x is zero ")

    case 4: 
        print("case is 4")

    case _ if x!=20:
        print( x,"case is not 20")

    case _ if x!=40:
        print(x,"case is not 40")            
    case _:
        print(x)