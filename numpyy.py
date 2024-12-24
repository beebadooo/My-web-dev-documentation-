# python -m pip install [packagename]
import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2,3,3,2,1],[4,5,6,7,8,9]])
'''
print(a.shape)  # 2 dim- returns (rows,colums)
print(a.dtype) #get type
print(a.itemsize) #get size
a.nbytes #get total size
'''

'''
#get a specific element [r,c]
print(b[1,1])

#get a specific row
print(b[0, :])

#get a specific column
print(b[:, 2])

#get by indexing [row index, start:stop:step]
print(b[1 , 1:5:2])

#change the value
b[: , 2] = [9,9]
print(b)
'''
'''
#3d array
c=np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(c[0,1,2]) #get specific element
print(c[:,1,:])
#replace
c[:,1,:]  = [[5,4,3],[9,8,7]]
print(c)
'''
'''
#all zeroes matrix
print(np.zeros((2,3,2)))
#all ones matrix
print(np.ones((2,3), dtype = 'int32'))

#any other number matrix
print(np.full((2,3),8 , dtype='float64')) #np.full((shape),value to be filled)

print(np.full_like(b,7)) #takes the shape of given array and fills it with the value given
#random decimal nos
print(np.random.rand(2,2), )

#random integer nos
print(np.random.randint(-1,7,size=(3,4))) #7 not included
'''
#an array
'''
x=np.ones((5,5),dtype='int')
y=np.zeros((3,3),dtype='int')
y[1,1] = 9
x[1:4,1:4] = y
print(x)
'''
#if we use b=a to copy array then original values of a changes, so use .copy()
'''
a=np.array([1,2,3])
b=a.copy()
b[1]=7
print(a,b) '''
######   Mathematics in numpy
'''
a=np.array([1,2,3,4])
print(a+2) #adds 2 to each element of array
print(a*2) #subtracts 2 from each elemant
print(a/2)
print(np.sin(a))  #sin of each element
'''

######  LINEAR ALGEBRA
'''
a=np.full((2,3),3)
b=np.full((3,2),5)
print(np.matmul(a,b))  #multiply the matrix

#find the determinant
c=np.identity(3)
print(np.linalg.det(c)) '''
######## STATS WITH NUMPY
'''
s=np.array([[1,2,3],[4,45,6]])
print(np.min(s,axis=1))
print(np.max(s,axis=0))
print(np.sum(s,axis=1))'''
####### reorganizing arrays
'''before=np.array([[1,2,3,4],[5,6,7,8]])
print(np.shape(before))
after = before.reshape((8,1))
print(after)'''
#vertically stacking vectors
v1=np.array([2,3,4,5])
v2=np.array([1,6,7,8])
print(np.vstack([v1,v2]))

#horizontally stacking vectors
h1=np.zeros((2,2))
h2=np.ones((2,4))
print(np.hstack([h1,h2]))