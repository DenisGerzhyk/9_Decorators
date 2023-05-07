# 9_Decorators

1). 
Decorator function decor_func takes in a function as an argument, and returns a new function called wrapper. The new function takes in a parameter 'n' and calls the original function with that parameter. If the parameter is even, it returns True. Otherwise, it returns False. The main function is decorated with this decorator using the @decor_func syntax, and it takes an integer input from the user and returns it. The decorated main function is called and prints the result.

2). 
Decorator function decor_func takes in a function as an argument and returns a new function called wrapper. The new function takes in a string parameter and removes all punctuation from it except for apostrophes. It then splits the string into a list of words and returns the first word. It also calls the original function with the string parameter before returning the result. The main_func function is decorated with this decorator using the @decor_func syntax and takes a string input from the user and prints the result.

3). 
Function some_gen takes in three arguments: begin, end, and func. It generates a sequence of values by repeatedly calling func on the value of begin, yielding the result, and updating begin to the yielded value. The pow function takes a single argument x and returns x squared. The some_gen function is called with begin=2, end=4, and func=pow, and the resulting sequence is converted to a list and printed.

4). 
Decorator function decor_func takes in a function as an argument and returns a new function called wrapper. The new function calls the original function and measures the time it takes to run it. It then prints the time and returns the result of the original function. The main_func function is decorated with this decorator using the @decor_func syntax, and it creates a list of squares of integers from 0 to 99999 and prints it. The decorated main function is called and the time it takes to run is printed.

5). 
Decorator function upper_func takes in a function as an argument and returns a new function called wrapper_func. The new function calls the original function with the argument, and then prints the uppercased version of the argument. The main_func function is decorated with this decorator using the @upper_func syntax, and it takes a string as input and prints it. The decorated main function is called with the argument "Hello World,im Devis" and prints "Hello World,im Devis" followed by "HELLO WORLD,IM DEVIS".

6). 
Decorator function memorize_func takes in a function as an argument and returns a new function called wrapper_func. The new function calls the original function with the argument, and then returns the hexadecimal representation of the result of the original function. The main_func function is decorated with this decorator using the @memorize_func syntax, and it takes an integer as input and returns its square. The decorated main function is called with the argument 2 and prints "0x4".

7). 
Decorator function type_func takes in a function as an argument and returns a new function called wrapper_func. The new function calls the original function with the argument, and then checks each element of the argument to see if it is an integer. If an element is not an integer, it returns a string containing the index of the element and its type. The main_func function is decorated with this decorator using the @type_func syntax, and it takes a list as input and returns it. The decorated main function is called with the argument [1, 4, 3, "Isk", 3, 2] and prints the original list, followed by the string "Its index <class 'str'> ----- Isk".

8).
This code defines a decorator function low_func that takes in a function as an argument and returns a new function called wrapper_func. When the decorated function main_func is called, it passes its argument to the decorated function and returns the original string in lowercase. The @low_func decorator is used to apply the low_func decorator to the main_func function. Finally, the main_func function is called with the string "Im Denis,i wanna say thank you,and Im 18" and the result "im denis,i wanna say thank you,and im 18" is printed.

9).
This code defines a decorator function decor that takes in a function as an argument and returns a new function called wrapper_func. When the decorated function main is called, it passes its argument to the decorated function and returns the squared value of the argument as a list. The @decor decorator is used to apply the decor decorator to the main function. Finally, the main function is called with the argument 2 and the result [4] is printed.

10).
This code defines a decorator function decor_func that takes in a function as an argument and returns a new function called wrapper_func. When the decorated function main_func is called, it passes its argument to the decorated function, returns the squared value of the argument and adds 10 to it. The @decor_func decorator is used to apply the decor_func decorator to the main_func function. Finally, the main_func function is called with the argument 5 and the result 35 is printed.

11).
This code defines a decorator function debug_func that takes in a function as an argument and returns a new function called wrapper. When the decorated function main is called, it passes its argument to the decorated function, prints the argument and then calculates the sum of the elements in the argument while printing the running total at each iteration. The @debug_func decorator is used to apply the debug_func decorator to the main function. Finally, the main function is called with the list [1, 4, 2] and the result is printed as follows:

1, Debug - 1
4, Debug - 5
2, Debug - 7

12).
This code defines a decorator function timeout_func that takes in an integer timeout as an argument and returns a decorator function that takes in a function as an argument and returns a new function called wrapper. When the decorated function main is called, it passes its argument to the decorated function and measures the execution time of the decorated function. If the execution time exceeds the timeout, a message is printed to indicate that the function took too long. Otherwise, each element of the list is printed along with the total execution time. The @timeout_func decorator is used to apply the timeout_func decorator to the main function with a timeout of 0.00001 seconds. Finally, the main function is called with a long list of integers and the result is printed. If the execution time is less than the timeout, each element of the list will be printed along with the total execution time. If the execution time is greater than the timeout, a message will be printed indicating that the function took too long.
