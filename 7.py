otric=0
chet=0
promej=0
unik=0
numbers=set()
for i in range(5):
    num = int(input('введите 5 чисел:'))
    if num<0:
        otric+=1
    if num%2==0:
        chet+=1
    if num in numbers:
        unik+=1
    else:
        numbers.add(num)
    if num > (-255) and num < 1025:
        promej += 1

print('отрицательных:', otric)
print('четных:', chet)
if promej == 5:
    print('все числа входят в промежуток [-256; 1024]')
else:
    print('не все числа входят в промежуток [-256; 1024]')
if unik==0:
    print('все числа уникальны')
else:
    print('не все числа уникальны')



