#1. Temperature Converter
#task:-Celcius--> Fahrenheit using Function

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(f))

else:
    print("Invalid choice!")


#2. Student grade Calculator
#task:- Take mark as a input, Calculate Average and assign grade

def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1} (out of 100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(mark)

average = calculate_average(marks)
grade = calculate_grade(average)

print("Average Marks:", average)
print("Grade:", grade)

if average < 40:
    print("Result: Fail")
else:
    print("Result: Pass")

#3. Even Odd and Prime Number Checker

def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")


def check_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

check_even_odd(number)

if check_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")