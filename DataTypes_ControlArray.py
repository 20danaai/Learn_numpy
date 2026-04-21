#Lesson 5
import numpy as np 
# Show Array Data Types
my_array1=np.array([1,2,3,5,4,6])
my_array2=np.array([1.2,3.5,2.3])
my_array3=np.array(["osama","ahmad saad",'esr'])
print(my_array1.dtype)#int64
print(my_array2.dtype)#float64
print(my_array3.dtype)#<U10 UniCode String
print('*'*30)
# Create Array With Specific Data Type
my_array4=np.array([1,2,3],dtype=float)# float or "float" or 'f
my_array5=np.array([1.2,3.4,5.6],dtype=int)#int or "int or 'i"
#my_array6=np.array(["osama","ahmad saad",'esr'],dtype=int# Value Error
print(my_array4.dtype)#float64
print(my_array5.dtype)#int64
print('*'*30)
#Change Date type 
my_array1=my_array1.astype('float')
print(my_array1.dtype)#float64
print(my_array1)#[1. 2. 3. 5. 4. 6.]
my_array7=np.array([0,3,4,5,60,4,0,0])
my_array7=my_array7.astype('bool')
print(my_array7.dtype)#bool
print(my_array7)#[False  True  True  True  True  True False False]
#test capacity
my_array8=np.array([100,200,300,400],dtype="f")
print(my_array8.dtype)#float32
print(my_array8[0].itemsize)# 4 Bytes
my_array8=my_array8.astype('float')# change to float64
print(my_array8.dtype)#float64
print(my_array8[0].itemsize)# 8 Bytes
