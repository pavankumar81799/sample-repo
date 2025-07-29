num = [1,4,3,1,2,3]
num2 = []
for i in num:
    if i not in num2:
        num2.append(i)
num2.sort()
num2.reverse()
print(f'The new list is :  {num2}')

