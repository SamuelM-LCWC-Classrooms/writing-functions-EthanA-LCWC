# You will define and write each function for the task in this file

def temperature_converter(temperature, unit):
    if unit == "C" or unit == "c":
        temperature = temperature * 1.8
        temperature += 32
        return f"{int(temperature)} F"
    elif unit == "F" or unit == "f":
        temperature -= 32
        temperature = temperature / 1.8
        return f"{int(temperature)} C"
    else:
        return "ERROR: The second argument must be 'C' or 'F'"
    
def reverse(string):
    if len(string) == 0:
        return string
    else:
        new_string = string[len(string)-1:len(string)]
        string = string[0:len(string)-1]
        return new_string + reverse(string)
    #letter_list = []
    #for i in string:
    #    letter_list.insert(0, i)
    #new_string = ""
    #for i in letter_list:
    #    new_string += i
    #return str(new_string)

def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    #num1 = 0
    #num2 = 1
    #for i in range(n-1):
    #    num3 = num1 + num2
    #    num1 = num2
    #    num2 = num3
    #return num3

print(temperature_converter(100, "c"))

print(reverse(""))

print(fibonacci(8))