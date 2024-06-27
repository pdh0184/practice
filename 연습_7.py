def dict_3X(n):
    dict = {}
    num = 1
    for i in range(1,n+1):
        if '3' in str(num):
            while '3' in str(num):
                num += 1

            if num % 3 == 0:
                num += 1
                dict[i] = num
                num += 1
            else:
                dict[i] = num
                num += 1
        
        else:
            if num % 3 == 0:
                num += 1
                if '3' in str(num):
                    num += 1
                    dict[i] = num
                    num += 1
                else:
                    dict[i] = num
                    num += 1
            else:
                dict[i] = num
                num += 1

    return dict

print(dict_3X(50))
a = 11
if a % 3 == 0 or '3' in str(a):
    print(a)
    print(a+1)
