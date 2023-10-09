def my_steps(n):
    if n < 1 or n > 25:
      raise ValueError("Out of bound!")
    def steps(n):
        if n <= 1:
            return 1
        return steps(n-2) + steps(n-1)

    return steps(n)

def counts(s):
    return my_steps(s)
