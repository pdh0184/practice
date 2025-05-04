def clock_array(num):
    array = []
    for i in range(num):
        unit = [1] * num
        array.append(unit)
# [[1, 2, 3, 4], 
#  [12, 13, 14, 5], 
#  [11, 16, 15, 6], 
#  [10, 9, 8, 7]] 16-9 = 4^2 - 3^2 = 7

#    [[1, 2, 3, 4, 5], 
#   [16, 17, 18, 19, 6], 
#   [15, 24, 25, 20, 7], 
#   [14, 23, 22, 21, 8], 
#   [13, 12, 11, 10, 9]] 25 - 16 = 5^2 - 4^2 =9

#    mazino = ((num*num)-((num-1)*(num-1)))

    i = 0 #row 
    j = 0 #colunm
    z = 1 #요소
    n = 1

    if i == 0:
        while j < num: # 시작
            array[i][j] = z
            j += 1
            z += 1
            

    while n <= 3:
        

        if (j-1) == (num - n): #아래
            while i < (num-n): 
                i += 1
                array[i][j-1] = z         
                z += 1

        if i == (num - n): #왼쪽 
            while j > n:
                j -= 1
                array[i][j-1] = z
                z += 1
                
            
        
        if j == n:#위쪽
            j -= 1
            while i > n: 
                i -= 1
                array[i][j] = z
                
                z += 1
            
        if i == n: #오른쪽
        
            while j < (num- n -1):
                j += 1
                array[i][j] = z

                z += 1
            j += 1


                
        
        n+=1
    return array
print(clock_array(6))
print('hi')
