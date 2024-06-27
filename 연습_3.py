def solution(arr):
#50 미만 짝수 , 50 이상 홀수 면 작업하지 않음
    qrr = []
    n = 0
    changed = True
    while changed:
        changed = False
        
        for i in arr:
            if (i >= 50 and i % 2 ==0):
                qrr.append(int(i/2))
            elif (i < 50 and i % 2== 1):
                qrr.append(i*2 + 1)
            else:
                qrr.append(i)       
        n += 1
        print(n)
        print(f"기존 :{arr}")
        print(f"변경 : {qrr}")
        if arr != qrr:
            arr = qrr
            qrr = []
            changed = True
        else:
            changed = False
    return n - 1

arr =[1, 2, 3, 100, 99, 98]
print(solution(arr))

#이 파이썬 코드를 응용해서 작성 (밑의 파이썬 코드는 배열의 변화가 없을때까지 작업을 진행 시키는 코드로 changed 변수를 False로 만들고 작업이 끝나는 부분에 change 변수를 True로 만듦 ) 
# def process_array(arr):
#     changed = True
#     while changed:
#         changed = False
#         for i in range(len(arr)):
#             if arr[i] < 10 and arr[i] % 2 == 0:
#                 arr[i] *= 2
#                 changed = True
#     return arr

# # 주어진 배열
# my_array = [1, 2, 3, 4, 5]

# # 배열을 변화시키는 작업 수행
# result_array = process_array(my_array)

# # 결과 출력
# print("변경된 배열:", result_array)