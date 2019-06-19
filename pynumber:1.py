import numpy as np

arr_rows=int(input("enter rows: "))
arr_col=int(input("enter column: "))

print("matrix shape is " + str(arr_rows) + "*" +str(arr_col))
z=np.random.rand(arr_rows,arr_col)

np.savetxt('array.txt',z)        #Saving the array to a file
np.loadtxt('array.txt')
