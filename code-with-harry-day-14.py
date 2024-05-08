# if - else  conditional statement 
# a = int( input("inter your number : ") )
# print(a)

# if a > 0:
#     print("positive")
# elif a < 0:
#     print("negative")
# else:
#     print("zero")    

# #  conditional statement 

# applePrice = 10
# budget = 200
# if (budget - applePrice > 50):
#     print("Alexa, add 1 kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")
  

#  elif 

# num = int(input("INTER OUR NUMBER  PLEASE : "))

# if ( num < 0):
    
#     print("negative")
# elif(num == 0):
#     print(" ZERO ")
# elif(num == 999):
#     print("  THE NUMBER IS SPECIAL !")          

# else:
#     print(" positive ")   


#  nested if- else 


num = int(input("pPLRASE INTER YOUR NUMBER "))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

