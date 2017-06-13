def fizz_buzz(n):
    """A function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', 
    or the argument it receives, all depending on the argument of 
    the function, a number that is divisible by, 3, 5, or both 3 
    and 5, respectively.
    """
    if type(n) == int:
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        else:
            return n
    else:
        return n
