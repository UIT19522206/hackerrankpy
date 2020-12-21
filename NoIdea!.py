from collections import Counter
[n,m] = list( map( int,input().split() ) )
numbers = list( map( int,input().split() ) )
A = list( map( int,input().split() ) )
B = list( map( int,input().split() ) )


def likes(numbers,A):   
    numbers_ = Counter(numbers) # elements and  numbers of its appearances in array
    elements = set(numbers_.keys()) # elements in array
    A = set(A) # set
    x = A.intersection(elements) # x is elements appear both in A and numbers
    total = 0
    for _ in x:
        total += numbers_[_]
    return total


def dislikes(numbers,B):
    numbers_ = set(numbers)
    B = set(B)
    x = B.intersection(numbers_)  
    x = set(x) 
    return x
print( Counter(numbers) )
print(likes(numbers,A))
print(dislikes(numbers,B))