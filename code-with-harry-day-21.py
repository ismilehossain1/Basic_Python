           
#  defult  argument  




def kona ( a=2,b=3 ):

    sum = a+b
    print(sum)

kona( 1,2) 

#   keyword argument  number 


def kona ( a=2,b=3 ):

    sum = a+b
    print(sum)

kona( b=2,a=3) 



#   required keyword argument
   

#   must be need value  with  out  it is not required 


def kona ( a=10,b=12 ):

    sum = a+b
    print(sum)

kona() 
print(" kona ")

#   harry  
# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


# def average(*numbers):
#   # print(type(numbers))
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   # print("Average is: ", sum / len(numbers))
#   # return 7
#   return sum / len(numbers)


# # average(4, 6)
# # average(b=9)

# c = average(5, 6, 7, 1)
# print(c)


def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")

def name(**kona): 
    print(type(kona))
    print("Hello,", kona["lol"], kona[" esfty "], kona[" imran"])
name( mname="Buchanan", lname="kona ",)
   
