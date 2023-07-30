text= input("enter the text")
span= False
if(" make a lot  of money" in text): span=True
elif("buy now" in text): span= True
elif("click this" in text): span= True
elif("subscribe this" in text): span=true
else: span=False
if(span): print("this text is spam")
else: print("this text is not spam ")