
class Rectangular():

    def __init__(self, y, b):
        self.y = y
        self.b = b

    @property
    def area(self):
        a = self.y * self.b
        self.a = a
        return a

    @property
    def perimeter(self):
        p = self.b + 2 * self.y
        self.p = p
        return p

    @property
    def radioh(self):
        rh = self.a / self.p
        return rh

    @property
    def anch_sup(self):
        return self.b

    @property
    def depthh(self):
        return self.y


class Trapezoidal():

    def __init__(self, y, b, z):
        self.y = y
        self.b = b
        self.z = z

    @property
    def area(self):
        a = (self.b + self.z * self.y) * self.z
        self.a = a
        return a

    @property
    def perimeter(self):
        p = self.b + 2*self.h * (1 + self.z ** 2) ** 0.5
        self.p = p
        return p

    @property
    def radioh(self):
        rh = self.a / self.p
        return rh

    @property
    def anch_sup(self):
        self.t= self.b + 2 * self.z * self.y
        return self.t

    @property
    def depthh(self):
        return self.a/self.t

# class Triangular():

#     def __init__(self, y, z):


# class Circular():

#     def __init__(self, y, d):



# class Parabolica():
    
#     def __init__(self, y):
#         super().__init__(y)


# class Rectesquina():
    
#     def __init__(self, y,b,r):
        


# class Trianesquina():
    
#     def __init__(self, y,z,r):

def parameters(channel_type):
    print("El área es: ",channel_type.area)
    print("El perimetro es: ",channel_type.perimeter)
    print("El radio hidráulico es: ",channel_type.radioh)
    print("El ancho superficial es: ",channel_type.anch_sup)
    print("La profundidad hidráulica es: ", channel_type.depthh)

def run():
    #Canal rectangular
    rect = Rectangular(2,2)
    parameters(rect)

    #canal trapezoidal
    trap = Trapezoidal(2,2,1)
    parameters(trap)

    #Canal Triangular

if __name__ == '__main__':
    run()


#Una línea de practica de commit