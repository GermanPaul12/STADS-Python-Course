# Exercise 1
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
#print(max_of_three(3, 6, -5))

# 2

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
#print(sum((8, 2, 3, 0, 7)))

# 3
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
#print(multiply((8, 2, 3, -1, 7)))

# 4
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
#print(string_reverse('1234abcd'))

# 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#n=int(input("Input a number to compute the factiorial : "))
#print(factorial(n))

# 6
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
#test_range(5)

# 7

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

#string_test('The quick Brown Fox')

# 8
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

#print(unique_list([1,2,3,3,3,3,4,5])) 

# 9
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
#print(test_prime(9))

# 10
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
#print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 11
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
#print(perfect_number(6))

# 12
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
#print(isPalindrome('aza')) 

# 13
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
#pascal_triangle(6) 

# 14
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
#print ( ispangram('The quick brown fox jumps over the lazy dog')) 

# 15
def hyphen_words(words):
    items=[n for n in words.split('-')]
    items.sort()
    return '-'.join(items)

#print(hyphen_words('Quick-Brown-Fox-Jumps-Over-The-Lazy-Dog'))

# 16
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
#printValues()

def subract_all(*args):
    return args[0] - sum(args[1:])

#print(subract_all(100, 1,2,3,4,4,5,6,3,2,2,4,5,5,3))

