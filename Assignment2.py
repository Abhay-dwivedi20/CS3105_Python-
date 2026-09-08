# #1.

# Full_name = input("Enter your name: ")
# print("welcome"+" "+Full_name)

# #2.

# Int_read = int(input("Enter an integer: "))
# print("The integer you entered is:", Int_read)

#3.

# val1 = int(input("Enter number: "))
# val2 = str(val1)
# val3 = float(val1)
# print(type(val1))
# print(type(val2))
# print(type(val3))
# val4 = int(val2)
# print(type(val4))
# val5= float(val2)
# print(type(val5))
# val6 = str(val3)
# print(type(val6))


# #4.

# num1 = float(input("Enter first number: "))
# print(round(num1))

# #5.


# num2 = float(input("Enter second number: "))
# print(round(num2,2)) #Round the digit upto 2 decimal places

# #6.

# print("Hello".ljust(10))    # Left
# print("Hello".rjust(10))    # Right
# print("Hello".center(10))   # Centre

#7.

# num_for_sqrt = int(input("Enter a number to find its square root: "))
# sqrt_value = num_for_sqrt ** 0.5
# print("The square root of", num_for_sqrt, "is:", sqrt_value)

# print(bin(round(sqrt_value)))
# print(hex(round(sqrt_value)))
# print(oct(round(sqrt_value)))

#8.

# str1 = input("Enter a string: ")
# print("The string you entered is:", str1*5)

#9.

# # Character value for a number
# n = int(input("Enter a number: "))
# print("Character:", chr(n))

# # ASCII value for a character
# ch = input("Enter a character: ")
# print("ASCII value:", ord(ch))

#10.

# sentence = input("Enter a sentence: ")
# print("lenght of the sentence is:", len(sentence))
# print("Length of the sentence without spaces is:", len(sentence.replace(" ", "")))
# words = sentence.split()
# print("Number of words in the sentence is:", len(words))

#11.

expression = '100*5+9+5**2'

result = eval(expression)

print("Result:", result)