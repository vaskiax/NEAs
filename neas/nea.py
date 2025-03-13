class NEA():
    def __init__(self, args):
        from numpy import cos, radians
        self.id = args['id']
        self.name = args['name']
        self.a = args['a']
        self.e = args['e']
        self.i = args['i']
        self.tisserand = 1/self.a + 2*(self.a*(1-self.e**2))**0.5*cos(radians(self.i))

    def __str__(self):
        return f'NEA: {self.id}'
