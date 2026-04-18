#I have now started learning the NumPy library.
import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array(my_list)
print(my_list[0])
print(my_array[0]) 
print("="*20)
#dimensions
a=np.array(10)
b=np.array([1,2])
c=np.array([[1,2],[3,4]])
d=np.array([[[20,80],[90,70],[60,50]]])
#number of dimensions
print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim) 
print("="*20)
my_cutom_array=np.array([1,2,3],ndmin=4)
print(my_cutom_array)
print(my_cutom_array.ndim)
print(my_cutom_array[0])
print(my_cutom_array[0,0,0,2])
