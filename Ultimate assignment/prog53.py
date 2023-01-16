alpha="abcdefghijklmnopqrstuvwxyz"
lst=[]
for i in range(len(alpha)):
    lst+=[alpha[i]*(i+1)]
print(lst)

#another approach
"""
alpha="abcdefghijklmnopqrstuvwxyz"
lst=[]
for i in range(len(alpha)):
    a=alpha[i]*(i+1)
    #print(a)
    lst.append(a)   #USING append
print(lst)
"""
