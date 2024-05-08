
# list most important things  

#  always start in 0  
# length 5 hobe but  index 4  hobe 



# lst=[1,2,"kona","ridu"] 
# print(lst)
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# # print(lst[4])  error :  show 


#  convertion  

lst = [2,2,3,"kona","ridu"]
print(lst[-3])
#  length 5 hobe but index 4 hobe so ans : len(5)- 3  = index(2) is  ans  so index 
print(lst[len(lst)-3]) 
print(lst[5-3])
print(lst[2])



# #   kono k iso khojeerr jonno  ayter useed kore (for integer)

# if 2 in lst :
#     print("yes")
# else:
#     print("no")    



# # fun thing  (for string )
 
# if "ko"in "kona ":
#     print("yes")

     
# #    all print  
# print(lst) 

# #   its call slising    index 1 thaika index 2 porjointoh print  korbo 

print(lst[1:2])
#   0 index thika index   ( len(lst)-1 )= 0:5-1 = 0:4    porjon tho jaibo 

print(lst[0:-1])
 
  

#  list er modde  loop  chalabo   
#    very very impoRTANT  

lst =  [ i for i in range(4)]
print(lst)
 
# lst =  [ i*i for i in range(4)]
# print(lst) 
 
 

# most  important  

lst = [ i==i for i in range(100) if (i/2) == 0]
print(lst) 
 

 