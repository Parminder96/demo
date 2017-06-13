str=input("enter a string")
i=0
j=len(str)-1
while i<len(str)-1:
    if str[i]==str[j]:
        i=i+1
        j=j-1
    else:
         print("not")
         break
if i==len(str)-1:
    print("p")

    
