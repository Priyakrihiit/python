myDict= {
    "fast": "in a quick manner",
    "priya": "a programmer",
    "marks": [45, 67, 87],
    "anotherDict": {'priya': 'web developer'}

}

print(list(myDict.keys()))  #printing keys of dictionary
print(list(myDict.values())) #printing the values of keys
print(list(myDict.items()))  #printing all items of dictionary
print(myDict)

#update the list of dictionary and adding items in it
updateDict= {
    "prerana": "friend",
    "priya": "dancer"
}
myDict.update(updateDict)
print(myDict)   
print(list(myDict.keys()))


#for getting some value from dictionary
print(myDict.get('priya'))
print(myDict.get('marks'))
print(myDict.get('sammi')) #return NONE becuase of unavailable



#practice set

dictionary={
    "pankha": "fan",
    "kitab": "book",
    "kalam": "pen",
    "thaila": "bag"
}
#take a input and give the results
print("options are ",dictionary.keys())
a=input("enter the hindi word\n")
'''print("the meaning of your word is : ", dictionary[a])'''  #it gives error if user gives input out of the dictionary
print("the meaning of your word is :" , dictionary.get(a))   #never gives error, it gives none










