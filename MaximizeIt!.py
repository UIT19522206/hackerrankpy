from itertools import product

[M,K] = list(map(int,input().split())) 
def initial(num):
    A = []
    sub_A_len = []
    for i in range(0,num):
        temple = list( map(int,input().split()[1:]) )
        A.append(temple)
        sub_A_len.append( len(temple) )
    max_Size = max(sub_A_len)
    for i in range( 0,len(A) ):
        if(len(A[i]) < max_Size ):
            temple = A[i]
            while( len(temple) < max_Size ):
                temple.append('kill')
            A[i] = temple
    return A
def index_arr(arr,num,k):
    res = 0
    size = len(arr[0])
    arr_index = list( product( list( range(0,size+1) ),repeat = num ) )
    for item in arr_index:
        Truth_item = True
        for i in range( 0,len(item) ):
            kills = arr[i].count('kill')
            numbers = len(arr[i]) - kills
            if(item[i] >= numbers):
                Truth_item = False
                break
        if(Truth_item):
            total = 0
            for i_ in range( 0,len(item) ):
                total += pow(arr[i_][item[i_]],2)
            if(total % k > res):
                res = total % k
            if( res == k-1 ):
                return res
    return res
A = initial(M)
B = index_arr(A,M,K)
print(B)