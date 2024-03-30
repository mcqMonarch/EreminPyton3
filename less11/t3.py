from turtle import *


class System:

    def __init__(self, s, a, w, angle):
        self.axiom = a
        pensize(w)
        self.len = s
        self.angle = angle
        self.axiom2 = a

    def draw(self):
        tracer(1, 0)

        for i in self.axiom2:
            if 'F' == i:
                forward(self.len)
            elif '+' == i:
                left(self.angle)
            else:
                right(self.angle)
        done()

    def repeat(self, x):
        for _ in range(x):
            self.axiom2 += '--' + self.axiom


snow = System(100, 'F+F--F+F', 5, 70)
snow.repeat(20)
snow.draw()
