def solution(n):
    i = 2
    z = 0
    arr = []
    while n != 1:
        if n % i == 0:
            arr.append(i)
            while n % i == 0:
                n /= i
            i += 1
        else:
            i += 1

    return arr

print(solution(19))
