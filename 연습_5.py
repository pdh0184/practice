#def solution(numbers):
result = ''
a = "twofourseven"	
num_eng ={"zero" : '0', "one" : '1', "two" : '2', "three": '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
while len(a) > 1:
    for i in num_eng:
        if a.startswith(i):
            result += num_eng[i]
            a = a[len(i):]

    
    # if a.startswith(i):
    #     result += num_eng[i]
    #     a = a.lstrip(i)
    # else:
    #     pass
    print(a)

print(result)