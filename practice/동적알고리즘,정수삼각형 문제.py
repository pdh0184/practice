'''
정수삼각형
   7
  3 8 
  8 1 0
 2 7 4 4
4 5 2 6 5
위에서부터 아래까지 내려가는데 가장 큰 합이 되도록

정답 =30
'''

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution_Bottom_UP(triangle):
    
    floor = len(triangle) - 1 #floor = 4
    
    while floor > 0: 

        for i in range(floor):
            
            triangle[floor-1][i] += max(triangle[floor][i] , triangle[floor][i+1])
        

        floor -= 1

    return triangle[0][0]

print(solution_Bottom_UP(triangle))
