stry=input("Enter word: ")
char_remove=input("Enter the char that you want to dalete :")
stry2=""
for i in stry:
    if i==char_remove:
        continue
    else:
        stry2+=i
print(stry2)