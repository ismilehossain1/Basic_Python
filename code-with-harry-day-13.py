#  string operation  lower case to uper case conversion 
# string well be immutable 
a = "ismile! !!!!! !!!!!"
b="kona11111111111"
ayoton = (len(a))
print(ayoton)
# upper lower 
print(a.upper())
print(a.lower())
# rstrip 
print(a.rstrip("!"))
print(b.rstrip("1")) 
# replace 
print(a.replace( "ismile ","kona") )

#  split ... must bneed speesh here 
print(a.split("."))
#  size bariya dise ar ki 
c= " hi  efty  the bad boy "
print(len(c))
print(len(c.center( 100 )))
#  find method 
d=" this is out of this world , amd he is out of your aleage "

print(d.find("is"))

#  isalnum- is itb the alpha numeric numbere
sart1="welcome to my hacking journy"
print(sart1.isalnum())
sart1="welcometomyhackingjourny"
print(sart1.isalnum())
#   we can used all things 


#   ispritable 
sart1="welcometomyhackingjourny"
print( sart1.isprintable() )
 
sart1="welcometomyhackingjourny \n"
print( sart1.isprintable() )

#  isspace

sart1="     "
print( sart1.isspace() )
 
sart1=""
print( sart1.isspace() )


#  most importan -- swapcase


sart1="welcome to my hacking journy"
print( sart1.swapcase() )   

sart1="welcome to my hacking journy"
print(sart1.upper() )


s="WELCOME TO MY HACKING JOURNY"
print(s.swapcase())
 



