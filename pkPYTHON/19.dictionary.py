myDict= {
    "fast": "in a quick manner",
    "priya": "a programmer",
    "marks": [45, 67, 87],
    "anotherDict": {'priya': 'web developer'}
}
print(myDict['fast'])

print(myDict['marks'])
myDict['marks']=[56, 78, 88]
print(myDict['marks'])
print(myDict['anotherDict']['priya'])


#practice set
favlang={}
a=input("enter ur fav lang pk :\n")
b=input("enter ur fav lang sk :\n")
c=input("enter ur fav lang vk :\n")
d=input("enter ur fav lang kk :\n")
favlang["pk"]=a
favlang["sk"]=b
favlang["vk"]=c
favlang["kk"]=d

print(favlang)