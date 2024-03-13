class Polygone:
    
    def __lt__(self,other) ->bool:
        return self.aire() < other.aire()

    def aire(self)->float:
        raise NotImplementedError
    
    def __repr__(self)-> str:
        
        return f"{self.__class__.__name__} d'aire {self.aire():2f}"


class Triangle(Polygone):
    def __init__(self,p1: complex,p2:complex,p3:complex):
        self.v1 =p2 - p1
        self.v2= p3 - p1
    
    def aire(self)-> float:
        return abs((self.v1.conjugate() * self.v2).imag)/2.0

class Quadrilatere(Polygone):
    def __init__(self,p1: complex,p2:complex,p3:complex,p4: complex):
        self.t1 = Triangle(p1,p2,p3)
        self.t2 = Triangle(p3,p4,p1)
    
    def aire(self)-> float:
        return self.t1.aire() + self.t2.aire()



polygones = [Triangle(0,4, 3j), Quadrilatere(0,2,2+ 2.5j, 2.5j)]
print(sorted(polygones))
print(max(polygones))