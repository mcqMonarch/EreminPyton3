import random
from turtle import *


class System:

    def __init__(self, t: Turtle, start, s, a, w, angle):
        self.t = t
        self.axiom = a
        self.t.pensize(w)
        self.len = s
        self.angle = angle
        self.axiom2 = a
        self.t.up()
        self.t.lt(90)
        self.t.setpos(start)
        self.t.down()
        self.k = []
        self.rules = {}

    def draw(self):
        tracer(1, 0)

        for i in self.axiom2:
            if 'F' == i:
                self.t.forward(self.len)
            elif '+' == i:
                self.t.left(self.angle)
            elif i == '-':
                self.t.right(self.angle)
            elif i == '[':
                self.k.append((self.t.xcor(), self.t.ycor()))
            elif i == ']':
                self.t.setpos(self.k.pop(-1))
            elif i == 'B':
                if random.randint(0, 10) > 4:
                    self.t.forward(self.len)
            elif i == 'C':
                self.k.append(self.t.pensize())
                r = random.randint(0, 10)
                if r < 3:
                    self.t.pencolor('brown')
                elif r < 6:
                    self.t.pencolor('#667900')
                else:
                    self.t.pencolor('magenta')
                self.t.pensize(4)
                self.t.forward(self.len - 10)
                self.t.pensize(self.k.pop(-1))

        done()

    def add_rules(self, rules):
        for k, v in rules:
            self.rules[k] = v

    def repeat(self, x):
        for _ in range(x):
            # self.axiom2 += '+' + self.axiom + "---"
            # self.axiom2 = self.axiom.replace('F', 'F+F--F+F')
            for k, v in self.rules.items():
                self.axiom2 = self.axiom2.replace(k, v)

    # snow = System(100, 'F+F--F+F', 5, 70)


# snow.repeat(20)
# snow.draw()
rules = (('F', 'BF'), ('C', 'F[+BC][--BC]'))
tortila = Turtle
tree = System(tortila(), (0, -100), 10, 'F-F-BBCC', 5, 70)
tree.add_rules(rules)
tree.repeat(12)
tree.draw()
print(tree.k)
