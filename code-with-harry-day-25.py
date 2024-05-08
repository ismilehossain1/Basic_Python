
tup_name = ( " kona ", " redu  ", " efty ","susu ", " monalisa ")
name = list(tup_name)
name[0] = " ismile "
name.pop(1) #removename.append(" sadat ")#  again back in to  tupel 
name. append(' SADAT ')
print(name) 


# tup_name = tuple (name) not  change the  tupel in the python with out create the bnew list 

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


#    some important  method   to  seay our codeing journy 

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)    
#  index and  count  in the coding 
