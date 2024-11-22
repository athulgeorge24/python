a=[12,32,43,37,17,16]
b=[36,25,97,56,75,88]

combine=a+b
odd_emp=[]
eve_emp=[]
for i in combine:
    if i%2==0:
        eve_emp.append(i)
    else:
        odd_emp.append(i)
odd_emp.sort()
eve_emp.sort()
print(combine)
print(odd_emp)
print(eve_emp)
comb=eve_emp+odd_emp
print(comb)
