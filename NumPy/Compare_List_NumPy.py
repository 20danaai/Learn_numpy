# lesson 2 
import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array([1,2,3,4,5])
print(my_list)
print(my_array)
print(id(my_list[0]))# Non_contiguous (slow)
print(id(my_list[1]))
print(id(my_array[0]))# Contiguous Memory(fast)
print(id(my_array[1]))# 
my_list_of_date=[1,2,'a','b',True,10,50]
my_array_of_date=np.array([1,2,'a','b',True,10.50])
print(type(my_list_of_date))#<class 'list'>
print(type(my_array_of_date))#<class 'numpy.ndarray'>
print(type(my_list_of_date[0]))#<class 'int'>
print(type(my_array_of_date[0]))#<class 'numpy.str_'>

my_array_of_date_2=np.array([1,2])
print(type(my_array_of_date_2[0]))#<class 'numpy.int64'>
my_array_of_date_3=np.array([1,2,10.50])
print(type(my_array_of_date_3[0]))#<class 'numpy.float64'>
