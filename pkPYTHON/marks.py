sub1= int(input("enter maths marks= "))
sub2= int(input("enter physics marks= "))
sub3= int(input("enter chemistry marks= "))

if(sub1<33 or sub2<33 or sub3<33) : print("fail")
elif((sub1+sub2+sub3)/3<45): print("third devision")
elif((sub1+sub2+sub3)/3<60): print("second devision")
else: print("first devision")

