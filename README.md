[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16248373)
# Writing functions

The following challenges will requrie you to define and write funcitons to meet the criteria

You will be told what names to give to functions and parameters

It is important you do this, or the automated tests will not run sucessfully and this will not be considered a pass

## Task 1 - Temperature converter

You should write a function which converts between Celcius and Fahrenheit

The function will be called temperature_converter and accept two arguments

The first argument should be called _temperature_ and will be an integer value represneting a temperature

The second argument will be called _unit_ and shoudl only take the values "C" or "F" for Celcius and Fahrenheit

The function should use this information to convert one temparature uint to antother

The funciton should return a string composed of the new value and the unit, with a space between them (such as "100 C")

Note - the conversion equation is $$F = (C \times \frac{9}{5}) + 32$$

##### Examples
```
temperature_converter(100, "C") -> "212 F"
temperature_converter(50, "C") -> "122 F"
temperature_converter(32, "F") -> "0 C"
temperature_converter(68, "F") -> "20 C"
```

## Task 2 - Recursive string reverse
You will write a function which takes in one argument as a string

The funciton will output the string reversed

The function must be recursive

The funciton must be called _reverse_ and take one argument called _string_

##### Examples:
```
reverse("hello") ➞ "olleh"
reverse("world") ➞ "dlrow"
reverse("a") ➞ "a"
reverse("") ➞ ""
```

## Task 3 - Recursive Fibonacci Numbers

Fibonacci numbers are created in the following way:
```
F(0) = 0
F(1) = 1
...
F(n) = F(n-2) + F(n-1)
```
Write a function that calculates the nth Fibonacci number.

##### Examples:
```
fib(0) ➞ 0
fib(1) ➞ 1
fib(2) ➞ 1
fib(8) ➞ 21
```

The function must be recursive, name the function _fib_ and have it take one interger argument called _N_
