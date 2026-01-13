#write a function to concert temparature from celsius in to faranit c/5=(f-32)9

celcius=100
def convertSelciusToFaranit(celcius):
      faranit = (celcius * 9/5) + 32
      return faranit
     
result =convertSelciusToFaranit(celcius)
print(result)     
      
#write a function to count how many times each digit appears:(Digit frequency count)for given number
num= 34526677443553
def frequency(num):
      num=str(num)
      same={}
      for i in num:
            if i in same:
                  same [i] +=1
            else:
                  same [i]=1
      return same

output = frequency(num)
print(output)
      
#Write a function to print all prime numbers between given range
def findPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def printPrimes(start, end):
    for n in range(start, end + 1):
        if findPrime(n):
            print(n)
printPrimes(10, 40)


#write a function to print fibonacci number for given range
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

fib_numbers = fibonacci(10)
print(fib_numbers)


#write a function to check the given two stings are palindrom or not
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar")) 
print(is_palindrome("hello"))
#Method based culculater engine
    #Addition
    #substraction
    #multiplication
    #devision
    
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
        
calc = Calculator()

print(calc.add(5, 3))       
print(calc.subtract(5, 3))  
print(calc.multiply(5, 3))  
print(calc.divide(5, 0))    
print(calc.divide(5, 2))  


 #Then use a loop-driven menu to run the culculator.
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if user_input == "add":
            print("Result:", Calculator().add(num1, num2))
        elif user_input == "subtract":
            print("Result:", Calculator().subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", Calculator().multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", Calculator().divide(num1, num2))
    else:
        print("Invalid input. Please try again.")