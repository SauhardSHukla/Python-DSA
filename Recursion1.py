def print_natural(num):
    if num == 0:
        return  # Base case: stop when num reaches 0
    else:
        print_natural(num - 1)  # Recursive call: print numbers up to num - 1 first
        print(num)  # After the recursive call, print the current number

num = 9
print_natural(num)  # Just call the function, no need to print its result

def fibs(num):
    if num==0 :
        return 0
    elif num==1:
        return 1
    else:
        fib1=fibs(num-1)
        fib2=fibs(num-2)
        sum_output=fib2+fib1
        return sum_output

num=7
fibs(num)


def fib_series(num):
    def fib(n):
        if n == 0:
            return 0  # fib(0) should return 0
        elif n == 1:
            return 1  # fib(1) should return 1
        else:
            fib1 = fib(n - 1)
            fib2 = fib(n - 2)
            sum_output = fib1 + fib2
            return sum_output

    for i in range(num + 1):
        print(fib(i), end=", ")

num = 7
fib_series(num)



