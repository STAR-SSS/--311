#5
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2 #формула Герона
print('p', a + b + c)
print('s',(p* (p-a)* (p-b)* (p-c)) )