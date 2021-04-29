# defining the fibonacci number
def fib(n):
    # if the fibonacci number is equal to 0 or 1
    if n == 0 or n == 1:
        # return the n value
        return n
    # or else
    else:
        # return the fibonacci number subtracted by 2 plus fibonacci number subtracted by 1
        return fib(n - 2) + fib(n - 1)


# code would only work for one variable, to have it work for 20, I did a for loop
# for very i value in the range of 20
for i in range(20):
    # code will print the fibonacci sequence then to have it next to each other i used the print function (end).
    print(fib(i), end=". ")
