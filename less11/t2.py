import turtle as t


def element(s):
    if s > 6:
        s3 = s // 3
        element(s3)
        t.lt(60)
        element(s3)
        t.rt(120)
        element(s3)
        t.lt(60)
        element(s3)
    else:
        t.fd(s)
        t.lt(60)
        t.fd(s)
        t.rt(120)
        t.fd(s)
        t.lt(60)
        t.fd(s)


t.speed(200)
for _ in range(3):
    t.lt(120)
    element(100)
t.mainloop()