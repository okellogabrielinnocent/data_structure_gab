# array(data_type, value list)
import array


arr = array.array('i',[1,2,3,4,5,6,7,8,9])

print("Then new printed array is :" end="")
for i in arange(0,4):
	print(arr[i], end="")

print("\r")

#inserting an array
# append():- This function is used to add the value mentioned in its arguments at the end of the array.
#insert(i,x) :- This function is used to add the value(x) at the ith position specified in its argument.


# using insert() to insert value at specific position
# inserts 5 at 2nd position

arr.insert(1,14)

print("\r")


# printing array after insertion
print("The array after insertion is : ", end="")
for i in range (0, 5):
	print (arr[i], end="")



# pop():- This function removes the element at the position mentioned in its argument and returns it.
# remove():- This function is used to remove the first occurrence of the value mentioned in its arguments.


# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2))


# using remove() to remove 1st occurrence of 1
arr.remove(1)


# index() :- This function returns the index of the first occurrence of value mentioned in arguments.
# reverse() :- This function reverses the array.

# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))

#using reverse() to reverse the array
arr.reverse()
 
# printing array after reversing
print ("The array after reversing is : ",end="")
for i in range (0,6):
    print (arr[i],end=" ")

# count Return the number of occurrences of x in the array.

print(arr.count(2))

# typecode :- This function returns the data type by which array is initialised.

print (arr.typecode)

# itemsize :- This function returns size in bytes of a single array element.

print (arr.itemsize)

# buffer_info() :- Returns a tuple representing the address in which array is stored and number of elements in it.

print (arr.buffer_info())

# extend(arr) :- This function appends a whole array mentioned in its arguments to the specified array.
arr2 = array.array('i',[1, 2, 3])

arr.extend(arr2) # using extend() to add array 2 elements to array 1

# fromlist(list) :- This function is used to append a list mentioned in its argument to end of array.
# tolist() :- This function is used to transform an array into a list. 

# initializing list
li = [1, 2, 3]

arr.fromlist(li)

# using tolist() to convert array into list
li2 = arr.tolist()


# check https://docs.python.org/3/library/array.html#module-array for more details





