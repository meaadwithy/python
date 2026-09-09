

name = "meaad"
age = 20
print(name) # type write in python str not string
print(type(age))
print(len("hello"))

print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
print("""'Oh no', she exclaimed, 'Ben's bike is broken!'""")

# for comment use #

--------------------
print(10 / 5) # result double not int 2.0

print(9 // 5) # result ignores the remainder 1
print(9 % 5) # result module int 4
print(7 // 3)    # This is the integer division operator
print(7 % 3)     # This is the remainder or modulus operator


print(square(3)) # give 9
print(sub(6, 4)) # subtract  6-4 =2

print(2 ** 3 ** 2)     # the right-most ** operator gets done first! so 3 ** 2 give 9 then 2 ** 9 give 512  
print((2 ** 3) ** 2)   # use parentheses to force the order you want! its same idea as int to the power of int

print(3.9999, int(3.9999)) # This doesn't round to the closest int!
print(3.0, int(3.0))
print(float("123.45"))
print(str(17))

-------------------
n = input("Please enter your name: ")
print("Hello", n)

