#Q11
'''
n=3
for i in range(n):
    for j in range(n):
        print(i,j)
'''
#Q12
'''
def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def printFibonacciSeries(n):
    print("Fibonacci Series till", n, "numbers:")
    for i in range(n):
        print(Fibonacci(i), end=" ")
n = int(input('Enter the number upto which you want fibonacci- '))
printFibonacciSeries(n)
'''
#Q13
'''
def common_no(list1, list2):
	result = False
	for x in list1:
		for y in list2:
			if x == y:
				result = True
				return result
	return result
	

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_no(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_no(a, b))
'''
#Q14
def sort_dict_by_value(d):
    # Sort dictionary in ascending order by value
    ascending = dict(sorted(d.items(), key=lambda item: item[1]))
    # Sort dictionary in descending order by value
    descending = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return ascending, descending

sample = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sorting the dictionary
ascending, descending = sort_dict_by_value(sample)

# Output the results
print("Original dictionary:", sample)
print("Sorted in ascending order:", ascending)
print("Sorted in descending order:", descending)
#Q15
'''
# Demonstrate 'sep',print,input attribute
a = input('enter a string-')
print("Python", "is", "awesome",a, sep="---")
print("1", "2", "3", sep=":")
# Demonstrating end attribute
print("This line ends with a space", end=" ")
print("and this continues on the same line.")
# Demonstrate replacement operator
name = "Alice"
age = 25
print("Hello, {}. You are {} years old.".format(name, age)) # Using .format()
print(f"Hello, {name}. You are {age} years old.") # Using f-string
'''