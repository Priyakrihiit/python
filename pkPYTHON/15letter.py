

letter='''
Dear <|name|>,
congratulations, you are eligible for data scientist. you did very well in interview. you are selected for this post. please join us before due date.
have a great day ahead, thanks and regards.
\ndate: <|date|>

'''
name=input("enter your name\n")
letter=letter.replace("<|name|>", name)
date=input("enter date\n")
letter=letter.replace("<|date|>", date)

print(letter)