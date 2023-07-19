#used to change the data type

a="456"
print(type(a))  #o/p str
a= int(a)
print(type(a))  #o/p  int
b=a+17
print(b)  #o/p 473


#it gives error because letters doesn't make integer form.
a="4afjkkl02"
print(type(a))
a= int(a)
print(type(a))
b=a+17
print(b)
