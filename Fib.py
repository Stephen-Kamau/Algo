# O(n) time | O(1) space
def FibNth(n):
    """
    Question:
    The Fibonacci sequence is defined as follows:
    the first number of the sequence is 0, the second number is 1,
    and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
    Write a function that takes in an integer n and returns the nth Fibonacci number.
    """
    default = [0,1]
    i = len(default)+1
    while i <=n:
        fib = default[0]+default[1]
        default[0] = default[1]
        default[1] = fib
        i+=1
    return default[1] if n>1 else default[0]

print(FibNth(34))
