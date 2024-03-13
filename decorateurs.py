import time
import functools
from functools import lru_cache
from collections.abc import Iterable

def chronometre(fonction):
    name = fonction.__name__
    @functools.wraps(fonction)
    def chrono_fonction(*args):
        t0=time.perf_counter()
        arg_str = ", ".join(repr(arg) for arg in args)
        result = fonction(*args)
        elapsed = time.perf_counter() - t0

        print(f"[{elapsed:0.8f}s] {name}({arg_str})")
        return result
    return chrono_fonction

@chronometre

def pause(secondes: int=1):
    """carpe diem"""
    time.sleep(secondes)
    return

@lru_cache #memoisation
def fibonacci(n: int ) -> int:
    """renvoi le nieme terme de la suite de fibonacci"""
    if n in [0,1]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


#pause(2)
#help(pause)
lru_cache(fibonacci(5))


def ajoute  (valeur, autre: float):
    match valeur:
        case [tuple()]:
            return tuple(elt +autre for elt in valeur)
        case [Iterable]:
            return list(elt +autre for elt in valeur)
        case [_]:
            return (elt + autre for elt in valeur)
        
print(ajoute(1,1.5))