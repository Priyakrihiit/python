a={}
print(type(a))   #form of dictionary/ not set


#set: non repetative
#an empty set can be created using below syntax:
b=set()
print(type(b))
b.add(4)
b.add(6)
b.add(7)
b.add(5)
print(b)      #can't add dictionary and list

#function
print(len(b))  #for printing lenght of set

b.remove(4)   #remove 4 from set / if i remove unavailable set items from set, it gives error
print(b)

print(b.pop())  #remove first item from set
print(b)

#s.clear()
#s.union()
#s.intersection() etc. are also the function of set



s={18, "18"}
print(s)  #here first is int, other is string 


s={}
print(type(s))   #dictionary

s=()
print(type(s))   #tuple

s=[]
print(type(s))  #list



