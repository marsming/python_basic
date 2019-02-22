

for n in range(2,10):
    print('n:',n)
    for x in range(2,n):
        print('x:',x)
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        #循环中没有找到元素
        print(n,'is a prime number')