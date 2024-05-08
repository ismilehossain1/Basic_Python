#   most important list method 
#  . apooend method
#  .sort method
#  . reverse method
#  p ( . index ) /// index ber korar  jonno  amra used 
#  p ( .count ) /// akti number joto ber  ase toto ber preant  korbe  
#  . insert method /// noton kiso insert  korle ayta used korte hobe 
#  . extent  method ()
#  jora lagano     k = i=m   // print  (  k )


list = [1,1,12,2, 3,3,3,42]

list.append(70)
list.sort()
list.remove(2)
list.reverse()
# print(list.index(1))
print(list.count(3))
#  ak ber thakle  0  print  korbe  like 2 
print(list.count(2))
print(list.count(1))
#    insert any new  things 
list.insert(1,100)
list.reverse()

#  jump index inm to the list 
# print(list[1:3:2])

#  noton list add korte ayta korte porbo 

m=[900,100,100000]
k=list+m
print( k)

#  must be print korte  hobe 
print (list)