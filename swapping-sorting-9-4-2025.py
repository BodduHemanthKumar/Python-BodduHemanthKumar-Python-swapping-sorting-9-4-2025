# Task:- 
# program to separate odd & even elements from list 

num = [1,4,2,7,6,3,5,8,9]
even = []
odd = []
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)
print("printing even first and printing odd next")
print(even+odd)


# program to separate unique elements from list and add "*" at EOL
num = [1,2,5,3,8,7,2,6,1,3]
unq_num = []
star = []
for i in num:
    if i not in unq_num:
        unq_num.append(i)
    else:
        star.append("*")
print(unq_num+star)