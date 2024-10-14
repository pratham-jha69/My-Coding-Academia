#Addresses of Elements in the Array




##The address of the first element can be obtained in several ways:

&arr[0]


arr



&arr



ptr



arr + 0



ptr + 0





##The address of the second element:


&arr[1]



arr + 1



ptr + 1


#Values of Elements in the Array



##The value at the address of the first element can be obtained in several ways:




*ptr




*(arr)




*(&arr[0])




*(ptr + 0)



##The value at the address of the second element:



*(&arr[1])




*(arr + 1)




arr[1]






#Summary




##For addresses:



&ptr ≠ *(&arr) = ptr = &arr = arr = &arr[0] = arr + 0 = ptr + 0



##For values:

*ptr = *(arr) = *(&arr[0]) = *(ptr + 0)

###This should help you understand the different ways to access addresses and values in an array using pointers and array indexing.
