#1.

print("Hello world")

#2.

name = "Abhay Dwivedi"
Branch = "CSE"
University = "NIT JSR"
Age = 21
Percentage_12 = 78
Hobbies = ["Coding", "Gym", "Reading", "Sports"]
print("My name is", name)
print("I am from", Branch, "branch")
print("I am studying in", University)
print("My age is", Age)
print("My percentage in 12th is", Percentage_12)
print("My hobbies are:")
for hobby in Hobbies:
    print("-", hobby)

#3.

num1 = 10
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2) 
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

#4.

var1 = "Abhay"
var2 = "Dwivedi"
print("before swapping: var1 =", var1, "and var2 =", var2)
temp = var1
var1 = var2
var2 = temp
print("after swapping: var1 =", var1, "and var2 =", var2)

#5.

x=10
print(5*x**2 + 10*x + 5 )
x=20
print(5*x**2 + 10*x + 5 )
x=15
print(5*x**2 + 10*x + 5 )

#6.

r=6
print("distance travelled by the wheel in one rotation is", 2*3.14*r)

#7. 

salary = 1000000
DA_allowance = 0.4 * salary
HR_allowance = 0.2 * salary
gross_salary = salary + DA_allowance + HR_allowance
print("Gross salary is:", gross_salary)

#8.

Amount = int(input("Enter the amount in rupees: "))
number_of_notes_100 = Amount // 100
number_of_notes_50 = (Amount % 100) // 50
number_of_notes_10 = (Amount % 50) // 10
print("Number of 100 rupee notes:", number_of_notes_100)
print("Number of 50 rupee notes:", number_of_notes_50)
print("Number of 10 rupee notes:", number_of_notes_10)




