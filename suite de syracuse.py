import doctest
def syracuse(n:int) -> "generator":
    """
    Calcul de la suite de syracuse
    >>> list(p for p in syracuse(28))
    [28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    
    yield(n)
    while n!=1:
        if n & 1 ==0:
            n=n//2
        else:
            n = n*3 +1
        yield n
def length(iterable):
    """
    renvoie la longueur d'une structure iterable finie
    """

    return sum(1 for _ in iterable)


a = length(syracuse(58))
b = next(i for i in range(1,50) if length(syracuse(i))>100)
print(b)
print(b)
doctest.testmod()