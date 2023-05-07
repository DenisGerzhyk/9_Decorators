# 1).

def decor_func(func):
    def wrapper(n):
        func(n)
        if n % 2 == 0:
            return True
        else:
            return False

    return wrapper


@decor_func
def main(n):
    return n


print(main(n=int(input("Input number:"))))


# 2).

def decor_func(func):
    def wrapper(str):
        import string
        for punc in str:
            if punc == "'":
                continue
            elif punc in string.punctuation:
                str = str.replace(punc, " ")
        str = str.split()
        return str[0]
        func(str)

    return wrapper


@decor_func
def main_func():
    print("END")


print(main_func(str=str(input("Input string:"))))


# 3).

def some_gen(begin, end, func):
    for i in range(end):
        value = func(begin)
        yield value
        begin = value


def pow(x):
    return x ** 2


print(list(some_gen(2, 4, pow)))

# 4).

import time


def decor_func(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()
        print(finish_time - start_time)

    return wrapper


@decor_func
def main_func():
    spisok = [i ** 2 for i in range(100000)]
    print(spisok)


main_func()


# 5).

def upper_func(func):
    def wrapper_func(x):
        func(x)
        print(x.upper())

    return wrapper_func


@upper_func
def main_func(x):
    print(x)


main_func("Hello World,im Devis")


# 6).

def memorize_func(func):
    def wrapper_func(i):
        func(i)
        return hex(func(i))

    return wrapper_func


@memorize_func
def main_func(i):
    return i ** 2


print(main_func(2))


# 7).

def type_func(func):
    def wrapper_func(listin):
        func(listin)
        for i in listin:
            if type(i) != int:
                return f"Its index {type(i)} -----  {i}"

    return wrapper_func


@type_func
def main_func(list):
    return list


print(main_func([1, 4, 3, "Isk", 3, 2]))


# 8).

def low_func(func):
    def wrapper_func(string):
        func(string)
        return string.lower()

    return wrapper_func


@low_func
def main_func(string):
    return string


print(main_func("Im Denis,i wanna say thank you,and Im 18"))


# 9).

def decor(func):
    def wrapper_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return [result]

    return wrapper_func


@decor
def main(x):
    return x ** 2


print(main(2))


# 10).

def decor_func(func):
    def wrapper_func(x):
        func(x)
        return func(x) + 10

    return wrapper_func


@decor_func
def main_func(x):
    return x ** 2


print(main_func(5))


# 11).

def debug_func(func):
    def wrapper(x):
        func(x)
        sum = 0
        for i in x:
            sum += i
            print(f"Debug - {sum}")

    return wrapper


@debug_func
def main(x):
    print(x)


main([1, 4, 2])

# 12).

import time


def timeout_func(timeout):
    def decorator(func):
        def wrapper(lst):
            start_time = time.time()
            func(lst)
            end_time = time.time() - start_time
            if end_time > timeout:
                print(f"Function took too long! Time elapsed: {end_time}")
            else:
                for i in lst:
                    print(i)
                print(f"Execution time: {end_time}")

        return wrapper

    return decorator


@timeout_func(0.00001)
def main(lst):
    for i in lst:
        time.sleep(0.000001)


main([57, 94, 23, 31, 92, 56, 69, 70, 36, 16, 11, 35, 8, 94, 24, 31, 66, 32, 68, 96, 92, 31, 55, 15, 95, 92, 67, 60, 54,
      87, 47, 87, 30, 21, 12, 61, 6, 67, 44, 37, 11, 29, 12, 28, 9, 37, 45, 2, 48, 1, 38, 67, 45, 57, 70, 52, 28, 87,
      16, 15, 32, 31, 20, 83, 38, 90, 45, 91, 19, 91, 85, 2, 95, 75, 46, 47, 66, 51, 43, 32, 73, 85, 28, 53, 32, 54, 85,
      24, 98, 75, 84, 77, 31, 4, 2, 22, 11, 89, 56, 92, 44, 28, 89, 52, 29, 27, 38, 41, 1, 98, 92, 56, 1, 47, 3, 94, 27,
      62, 29, 51, 36, 41, 13, 21, 97, 83, 33, 35, 81, 12, 16, 1, 51, 75, 77, 10, 68, 44, 32, 52, 98, 60, 3, 7, 15, 17,
      74, 73, 81, 70, 25, 80, 8, 84, 68, 91, 4, 61, 81, 47, 64, 62, 9, 55, 31, 80, 47, 67, 35, 62, 13, 5, 25, 50, 58,
      66, 45, 77, 17, 47, 11, 61, 23, 78, 67, 94, 26, 31, 89])
