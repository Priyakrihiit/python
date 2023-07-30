#create a list using []
a=[1, 2, 3, 4, 5, 6]

#print the list using print() function
print(a)

#access using index using a[0] a[1] a[2] etc.
print(a[4])

#change the value of list-using
a[0]=67
print(a)

#we can create a list with items of different types
c=[45, "priya", False, 6.9]
print(c)
print(type(c))

#list slicing
friends=["rashmi", "kajal", "pooja", "divya", "surbhi", "prerana" , 40]
print(friends[2:6])

l1=[1, 3, 9, 76, 45]
l1.sort() #for sorting in ascending
print(l1)
l1.reverse() #for reversing
print(l1)
l1.append(56) #for adding at the end of the list
print(l1)
l1.insert(0, 999) #for addding at starting of the list
print(l1)
l1.pop(5) #for removing data by index number
print(l1)
l1.remove(9) #for removing any number or data
print(l1)




