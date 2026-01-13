#function
x="Hello Python"
def HelloPython():
    print(x);

HelloPython();


#global function
def firstFunction():
    global x;
x="all Good"

firstFunction();
print("How are you?"+x);

